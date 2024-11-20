import apache_beam as beam


class CountWords(beam.DoFn):
    def process(self, element):
        text = element.strip()  # Supprimer les espaces au début et à la fin
        words = text.split()  # Diviser le texte en mots
        for word in words:
            yield (word.lower(), 1)  # Émettre chaque mot avec une valeur de 1


with beam.Pipeline() as pipeline:
    word_counts = (
            pipeline
            | 'ReadTextFile' >> beam.io.ReadFromText(
        'venv/Python_level_6_DS/input.txt')  # Remplacez 'input.txt' par le chemin de votre fichier texte
            | 'CountWords' >> beam.ParDo(CountWords())
            | 'SumCounts' >> beam.CombinePerKey(sum)
    )

    # Écriture des résultats dans un fichier texte
    word_counts | 'WriteCounts' >> beam.io.WriteToText('word_counts.txt')
