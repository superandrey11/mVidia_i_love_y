import DataUtils
import VectorizationUtils
import SearchUtils
import NormalizationUtils
import Masks
from ResultCollector import Collector, CharacteristicsCollector

def search_characteristics(text):
    collector = CharacteristicsCollector()
    for subcat_id, search_fields in Masks.subcategory_search_masks.items():
        if SearchUtils.words_contains_in_text_OR_AND(text, search_fields):
            one_find = False
            for code in DataUtils.subcat_characteristic_map[subcat_id]:
                if code in Masks.characteristic_masks and SearchUtils.words_contains_in_text_OR_AND(TEXT_words, Masks.characteristic_masks[code]):
                    one_find = True
                    collector.collect(code)
            if not one_find and subcat_id in Masks.subcategory_default: collector.collect(Masks.subcategory_default[subcat_id])
    return collector


for test_category in DataUtils.testing_categories:
    category_comments_data = DataUtils.get_category_comments_data(test_category)
    category_characteristics_data = DataUtils.get_category_characteristicts_data(test_category)
    total_count = len(category_comments_data)
    print("PROCESS CATEGORY:" + str(test_category))
    counter = 0
    collector = Collector()
    for index, row in category_comments_data.iterrows():
        counter +=1
        if index % 300 == 0: print(str(counter*100/total_count) + " %")
        TEXT = row['TEXT']
        BENEFITS = row['BENEFITS']
        DRAWBACKS = row['DRAWBACKS']
        TEXT_words = NormalizationUtils.get_dict_words(TEXT)
        BENEFITS_words = NormalizationUtils.get_dict_words(BENEFITS)
        DRAWBACKS_words = NormalizationUtils.get_dict_words(DRAWBACKS)
        collector_ch = search_characteristics(TEXT)
        collector.addCollector(row["PRODUCT"], collector_ch)
    print(collector.calculate_total())









