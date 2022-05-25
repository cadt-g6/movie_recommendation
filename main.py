import pandas as pd
from lib.types.dataset_type import DatasetType
from models.contentbased_model import contentbased_model
from models.reRank_model import reRank_model


metadata = pd.read_csv(DatasetType.movies_metadata.original_path(prefix="."),low_memory=False)


data = pd.DataFrame([[1, 'Fake Movie', 'action adventure'],
                    [2, 'A', 'horror'],
                    [3, 'B', 'adventure'],
                    [4, 'C', 'family'],
                    [5, 'D', 'action adventure'],
                    [6, 'E', 'adventure horror'],
                    [7, 'F', 'action adventure family horror'],
                    [8, 'G', 'horror'],
                    [9, 'H', 'action family'],
                    [10, 'I', 'action adventure horror'],
                    [11, 'J', 'action adventure family'],
                    [12, 'K', 'horror family action']],
        columns = ['id','title','genres'])
print(data)

# a = contentbased_model('Toy Story',metadata)
# # print(a.basedOnOverview())
# # print(a.basedOnGenres())

b = reRank_model('Fake Movie',data)
print(b.reRankBasedOnUserInterest())