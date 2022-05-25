import pandas as pd
from lib.types.dataset_type import DatasetType
from models.contentbased_model import contentbased_model


metadata = pd.read_csv(DatasetType.movies_metadata.original_path(prefix="."),low_memory=False)

a = contentbased_model('Toy Story',metadata)
print(a.basedOnOverview())
# print(a.basedOnGenres())