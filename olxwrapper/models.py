from requests.structures import CaseInsensitiveDict
from dataclasses import dataclass
from typing import List, Optional, Any, Dict


@dataclass
class Result:
    status_code: int
    headers: CaseInsensitiveDict
    data: List[Dict]


@dataclass
class Category:
    id: int
    type: str


@dataclass
class Contact:
    name: str
    phone: bool
    chat: bool
    negotiation: bool
    courier: bool


@dataclass
class Rock:
    offer_id: Optional[str]
    active: bool
    mode: str


@dataclass
class Delivery:
    rock: Rock


@dataclass
class City:
    id: int
    name: str
    normalized_name: str


@dataclass
class Location:
    city: City
    region: City


@dataclass
class Map:
    zoom: int
    lat: float
    lon: float
    radius: int
    show_detailed: bool


@dataclass
class Value:
    label: str
    converted_value: Optional[Any] = None
    converted_previous_value: Optional[Any] = None
    previous_value: Optional[Any] = None
    converted_currency: Optional[Any] = None
    key: Optional[Any] = None
    value: Optional[int] = None
    type: Optional[str] = None
    arranged: Optional[bool] = None
    budget: Optional[bool] = None
    currency: Optional[str] = None
    negotiable: Optional[bool] = None


@dataclass
class Param:
    key: str
    name: str
    type: str
    value: Value


@dataclass
class Photo:
    id: int
    filename: str
    rotation: int
    width: int
    height: int
    link: str


@dataclass
class Promotion:
    highlighted: bool
    urgent: bool
    top_ad: bool
    options: List[Any]
    b2c_ad_page: bool
    premium_ad_page: bool


@dataclass
class Safedeal:
    weight: int
    weight_grams: int
    status: str
    safedeal_blocked: bool
    allowed_quantity: List[Any]


@dataclass
class Shop:
    subdomain: None


@dataclass
class User:
    id: int
    created: str
    other_ads_enabled: bool
    name: str
    logo: None
    logo_ad_page: None
    social_network_account_type: str
    photo: None
    banner_mobile: str
    banner_desktop: str
    company_name: str
    about: str
    b2c_business_page: bool
    is_online: bool
    last_seen: str
    seller_type: None
    uuid: str


@dataclass
class Offer:
    id: int
    url: str
    title: str
    last_refresh_time: str
    created_time: str
    valid_to_time: str
    pushup_time: None
    description: str
    promotion: Promotion
    params: List[Param]
    key_params: List[Any]
    business: bool
    user: User
    status: str
    contact: Contact
    map: Map
    location: Location
    photos: List[Photo]
    partner: None
    category: Category
    delivery: Delivery
    safedeal: Safedeal
    shop: Shop
    offer_type: str

    @property
    def price(self) -> Optional[float]:
        for param in self.params:
            if param.type == "price" and param.key == "price" and param.value:
                return float(param.value.value)
        return None


@dataclass
class Link:
    href: str


@dataclass
class Links:
    self: Link
    next: Optional[Link]
    first: Link


@dataclass
class Source:
    organic: List[int]


@dataclass
class Metadata:
    total_elements: int
    visible_total_count: int
    promoted: List[Any]
    search_id: str
    source: Optional[Source]


@dataclass
class OffersResult:
    data: List[Offer]
    metadata: Metadata
    links: Links
