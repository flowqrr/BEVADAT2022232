import pandas as pd


class NJCleaner:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def order_by_scheduled_time(self) -> pd.DataFrame:
        sorted_df = self.data.sort_values('scheduled_time')
        return sorted_df

    def drop_columns_and_nan(self) -> pd.DataFrame:
        self.data = self.data.drop(['from', 'to'], axis=1)
        self.data = self.data.dropna()
        return self.data

    def convert_date_to_day(self) -> pd.DataFrame:
        self.data['day'] = pd.to_datetime(self.data['date']).dt.day_name()
        self.data = self.data.drop('date', axis=1)
        return self.data

    def convert_scheduled_time_to_part_of_the_day(self) -> pd.DataFrame:
        """4:00-7:59 -- early_morning
         8:00-11:59 -- morning
         12:00-15:59 -- afternoon
         16:00-19:59 -- evening
         20:00-23:59 -- night
         0:00-3:59 -- late_night """

        def part_of_the_day(time):
            hour = int(time.split(' ')[1].split(':')[0])
            if 4 <= hour <= 7:
                return 'early_morning'
            elif 8 <= hour <= 11:
                return 'morning'
            elif 12 <= hour <= 15:
                return 'afternoon'
            elif 16 <= hour <= 19:
                return 'evening'
            elif 20 <= hour <= 23:
                return 'night'
            else:
                return 'late_night'

        part_of_day_df = self.data.copy()
        part_of_day_df['part_of_the_day'] = part_of_day_df['scheduled_time'].apply(part_of_the_day)
        return part_of_day_df.drop('scheduled_time', axis=1)

    def convert_delay(self) -> pd.DataFrame:
        delay_df = self.data.copy()
        delay_df['delay'] = (delay_df['delay_minutes'] >= 5).astype(int)
        return delay_df

    def drop_unnecessary_columns(self) -> pd.DataFrame:
        return self.data.drop(['train_id', 'actual_time', 'delay_minutes'], axis=1)

    def save_first_60k(self, path: str) -> pd.DataFrame:
        self.data[:60000].to_csv(path, index=False)
        return self.data

    def prep_df(self, path: str = 'data/NJ.csv'):
        self.order_by_scheduled_time()
        self.drop_columns_and_nan()
        self.convert_date_to_day()
        self.convert_scheduled_time_to_part_of_the_day()
        self.convert_delay()
        self.drop_unnecessary_columns()
        self.save_first_60k(path)

