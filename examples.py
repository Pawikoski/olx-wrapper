from olxwrapper.base import OLX


class Example:
	def __init__(self):
		self.olx = OLX()
		self.olx.limit = 40  # Set custom limit (default is 16)

	def offers_by_user_id(self, user_id):
		"""Lists all user's offers"""
		for offers in self.olx.fetch_offers(user_id=user_id, sort_by="price"):
			for offer in offers:
				print(offer.url)
				print(f"{offer.title} ({offer.price} zł) - {offer.location.city.name}\n")


if __name__ == "__main__":
	example = Example()
	example.offers_by_user_id(83867881)


