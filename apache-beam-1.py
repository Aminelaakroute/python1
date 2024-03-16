import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class FilterLines(beam.DoFn):
    """A DoFn class that filters lines containing a specific keyword."""
    def __init__(self, keyword):
        self.keyword = keyword

    def process(self, element):
        """Processes each element (line) to filter based on the keyword."""
        if self.keyword in element:
            yield element

def run_beam(input_file, keyword):
    output_file = 'output.txt'  # Adjusted to output to 'output.txt' directly
    # Define the pipeline options
    options = PipelineOptions()

    # Define the pipeline
    with beam.Pipeline(options=options) as p:
        (p
         | 'ReadLines' >> beam.io.ReadFromText(input_file)
         | 'FilterKeyword' >> beam.ParDo(FilterLines(keyword))
         | 'WriteResults' >> beam.io.WriteToText(file_path_prefix=output_file[:-4],  # Remove .txt for Beam's naming
                                                 file_name_suffix='.txt',
                                                 num_shards=1,
                                                 shard_name_template='')
        )

class BeamApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.input_file = TextInput(hint_text='Input file name', size_hint_y=None, height=30)
        self.keyword = TextInput(hint_text='Keyword', size_hint_y=None, height=30)
        run_button = Button(text='Run Beam Pipeline', on_press=self.run_pipeline, size_hint_y=None, height=50)

        self.layout.add_widget(self.input_file)
        self.layout.add_widget(self.keyword)
        self.layout.add_widget(run_button)

        return self.layout

    def run_pipeline(self, instance):
        input_file = self.input_file.text
        keyword = self.keyword.text
        run_beam(input_file, keyword)

if __name__ == '__main__':
    BeamApp().run()
