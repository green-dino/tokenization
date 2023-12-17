import nltk
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
import pandas as pd

def analyze_paragraph_structure(paragraph, method='charting'):
    # Tokenize the paragraph into sentences
    sentences = sent_tokenize(paragraph)

    # Tokenize each sentence into words
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]

    # Analyze based on the chosen method
    if method == 'charting':
        analyze_charting_method(tokenized_sentences)
    elif method == 'feature_matrix':
        analyze_feature_matrix_method(tokenized_sentences)
    else:
        print("Invalid method specified. Choose 'charting' or 'feature_matrix'.")

def analyze_charting_method(tokenized_sentences):
    relationships = []
    for i, sentence_tokens in enumerate(tokenized_sentences):
        if i < len(tokenized_sentences) - 1:
            relationships.append((sentence_tokens[-1], tokenized_sentences[i + 1][0]))

    if relationships:
        df = pd.DataFrame(relationships, columns=['Current Word', 'Next Word'])
        plt.figure(figsize=(8, 6))
        heatmap = sns.heatmap(pd.crosstab(df['Current Word'], df['Next Word']), cmap="YlGnBu", annot=True, fmt='g')
        plt.title('Relationships Between Tokens (Charting Method)')
        plt.show()

def analyze_feature_matrix_method(tokenized_sentences):
    # Your feature matrix analysis logic here
    # This could involve creating a table or chart to compare features of different entities or products
    # For simplicity, let's just print the sentences for now
    for i, sentence_tokens in enumerate(tokenized_sentences):
        print(f"Entity {i+1} features: {sentence_tokens}")

if __name__ == "__main__":
    paragraph = """
    The Charting Method:
    Organize information into tables or charts with rows and columns.
    Useful for comparing and contrasting different aspects of a topic.
    The charting method allows research in compared to tables. We're information organized with rose and columns for a side-by-side comparison and different aspects of each topic this method helps. Analyze multiple entities are variables with clear, visual representations of similarities and differences. Additionally, you can create a timeline chart that organizes information chronologically with Rosa rivers of time. And columns, displaying relevant events or milestones.
    The feature matrix charting method is great for organizing information related to the features of different entities or products rose represent items, collins, highlight features or attributes. This is great for comparing product, comparisons or systemic analysis of strength and weaknesses of each option.
    """

    analyze_paragraph_structure(paragraph, method='charting')
    analyze_paragraph_structure(paragraph, method='feature_matrix')
