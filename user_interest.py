from lib.types.dataset_type import DatasetType
from lib.types.source_type import SourceType
from lib.utils.utils import print_dict
from lib.services.user_interest_service import UserInterestService

service = UserInterestService(user_id=123963, source_prefix=".")
interest = service.exec()

print_dict(interest)
