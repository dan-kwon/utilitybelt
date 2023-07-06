import requests
import pandas as pd

class Canvas():
    """

    Parameters
    ----------

    Attributes
    ----------

    """
    def __init__(self, canvas_id, api_key):
        # api parameters
        url = "https://rest.iad-02.braze.com/canvas/details"
        headers = {"Authorization": f"Bearer {api_key}"}
        params = {"canvas_id": f"{canvas_id}"}
        # get details
        response = requests.get(
            url,
            headers=headers,
            params=params
        )
        self.canvas_id   = canvas_id
        self.api_key     = api_key
        self.canvas_name = response.json()['name']
        self.created_at  = response.json()['created_at']
        self.updated_at  = response.json()['updated_at']
        self.first_entry = response.json()['first_entry']
        self.last_entry  = response.json()['last_entry']
        self.messages    = [(i['name'],i['id']) for i in response.json()['steps'] if 'message' in i['type']]
        return
    
    def get_canvas_details()
        """
        Use this endpoint to export metadata about a Canvas, such as the name, time created, current status, and more.
        More info: https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_details/
        
        Parameters
        ----------
        canvas_id: string
            Canvas ID for use with Braze API.

        Attributes
        ----------
        Returns a pandas dataframe 
        """

        # api parameters
        url = "https://rest.iad-02.braze.com/canvas/details"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"canvas_id": f"{self.id}"}

        # get details
        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        return response

    def get_data_series(self, ending_at, starting_at, include_variant_breakdown=False, include_step_breakdown=False):
        """
        
        Use this endpoint to export time series data for a Canvas.
        More info: https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_analytics/
        
        Parameters
        ----------
        ending_at: Datetime (ISO-8601 string)
            Date on which data export should end.
        starting_at: Datetime (ISO-8601 string)
            Date on which data export should begin.
        include_variant_breakdown: boolean
            Whether or not to include variant statistics (defaults to false).
        include_step_breakdown: boolean
            Whether or not to include step statistics (defaults to false).

        Attributes
        ----------
        Return a pandas dataframe 
        """

        # api parameters
        url = "https://rest.iad-02.braze.com/canvas/data_series"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {
            "canvas_id": f"{self.id}",
            "ending_at": f"{str((pd.Timestamp('2023-07-02T23:59:59')).strftime('%Y-%m-%dT%H:%M:%S-8:00'))}",
            "starting_at": f"{str((pd.Timestamp('2023-07-01T00:00:00')).strftime('%Y-%m-%dT%H:%M:%S-8:00'))}",
            "include_variant_breakdown": "false"
        }

        # get details
        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        df = pd.json_normalize(
            response.json()['data'],
            record_path=['stats'],
            meta=[
                ['name']
            ]
        )

        self.data_series = df
        return

test_canvas = Canvas(
    id = 'af0a4eab-2bdf-47cf-b6d5-4f739c54132d',
    api_key = '01fd5009-543a-4239-8bfa-bf4903d28605'
)

test_canvas.get_canvas_details()

print(test_canvas.data_series)