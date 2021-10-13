from toggle_aggregation.models.toggle_df import ToggleFrame


def print_toggle_data():
    toggle_file_name = "toggle_september.csv"
    toggle_frame = ToggleFrame(toggle_file_name)
    toggle_frame.print_aggregated_descriptions()


if __name__  == "__main__":
    print_toggle_data()