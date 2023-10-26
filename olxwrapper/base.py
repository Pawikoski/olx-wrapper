import requests

from .models import Result, Offer, OffersResult
from typing import Dict, Iterator, List

from dacite import from_dict


class OLX:
	def __init__(self):
		self.base_url = "https://www.olx.pl/api/v1"
		self.limit = 16

	def _request(self, method: str, endpoint: str, params: dict = None, json: dict = None, data: dict = None) -> dict:
		url = f"{self.base_url}{endpoint}/"
		response = requests.request(method=method, url=url, params=params, json=json, data=data)  # TODO: catch exceptions
		data = response.json()
		return {
			"status_code": response.status_code,
			"headers": response.headers,
			"data": data
		}

	def get(self, endpoint: str, params: Dict):
		return self._request(method="get", endpoint=endpoint, params=params)

	@staticmethod
	def build_params(possible_params: dict) -> dict:
		params = dict()
		for param_key, param_value in possible_params.items():
			if param_value or param_value == 0:
				params[param_key] = param_value
		return params

	@staticmethod
	def validate_sort_option(sort_by: str, desc: bool):
		sorting_direction = "desc" if desc else "asc"
		allowed_sorting_methods = ["created_at", "price"]
		if sort_by not in allowed_sorting_methods:
			raise ValueError(f"Invalid sorting method. Allowed values are: {', '.join(allowed_sorting_methods)}")
		return f"{sort_by}:{sorting_direction}"

	def fetch_offers(self, user_id: int = None, query: str = None, sort_by: str = "created_at", sort_desc: bool = True) -> Iterator[List[Offer]]:
		endpoint = '/offers'
		sort_by_str = self.validate_sort_option(sort_by, sort_desc)
		params = self.build_params({"user_id": user_id, "query": query, "sort_by": sort_by_str, "offset": 0})
		while True:
			raw_result = self.get(endpoint=endpoint, params=params)
			result = from_dict(OffersResult, raw_result['data'])
			yield result.data
			if not result.links.next:
				break
			params["offset"] = params["offset"] + self.limit
