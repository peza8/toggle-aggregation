import os
from typing import List

import pandas as pd
import numpy as np
from pprint import pprint


class ToggleFrame:
    DATA_INPUT_DIR = "data-input"
    
    def __init__(self, csv_src_name: str) -> None:
        src_file_path = os.path.join(self.DATA_INPUT_DIR, csv_src_name)
        self.toggle_df = pd.read_csv(src_file_path)
        
        # Computed attributes
        self.aggregated_descriptions = self._aggregate_descriptions()
        pass

    def print_aggregated_descriptions(self):
        pprint(self.aggregated_descriptions)

    def _aggregate_descriptions(self) -> dict:
        unique_descriptions = self._get_unique_descriptions()

        for description in unique_descriptions:
            filtered_frame = self.toggle_df[self.toggle_df["Description"] == description]
            durations = filtered_frame["Duration"].to_numpy()
            total_duration = self._sum_duration_strs(durations)
            unique_descriptions[description] = total_duration

        return unique_descriptions

    def _get_unique_descriptions(self) -> dict:
        descriptions = self.toggle_df["Description"].to_numpy()
        # Hash map is fast for lookup
        unique_descriptions = {}
        for description in descriptions:
            if unique_descriptions.get(description) is None:
                unique_descriptions[description] = 0
        
        return unique_descriptions
    
    def _sum_duration_strs(self, duration_strs: List[str]) -> float:
        total_hours = 0
        for duration_str in duration_strs:
            time_components = duration_str.split(":")
            hours = float(time_components[0])
            minutes = float(time_components[1])
            sum_hours = hours + (minutes/60.0)
            total_hours += sum_hours
        return round(total_hours, 2)

    def _aggregate_tags(self) -> dict:
        pass