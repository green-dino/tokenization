import nltk
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
import pandas as pd

def analyze_paragraph_structure(paragraph, method='charting', entity_number=None):
    # Tokenize the paragraph into sentences
    sentences = sent_tokenize(paragraph)

    # Tokenize each sentence into words
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]

    # Analyze based on the chosen method
    if method == 'charting':
        analyze_charting_method(tokenized_sentences)
    elif method == 'feature_matrix':
        analyze_feature_matrix_method(tokenized_sentences, entity_number)
    elif method == 'flow':
        analyze_flow_method(tokenized_sentences)
    else:
        print("Invalid method specified. Choose 'charting', 'feature_matrix', or 'flow'.")

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

def analyze_feature_matrix_method(tokenized_sentences, entity_number):
    if entity_number is not None and 0 < entity_number <= len(tokenized_sentences):
        while True:
            # Print features of the selected entity
            selected_entity_features = tokenized_sentences[entity_number - 1]
            print(f"\nFeatures of Entity {entity_number}: {selected_entity_features}")

            # Ask the user for additional options
            print("\nAdditional options:")
            print("1. Analyze another entity")
            print("2. Return to the main menu")
            choice = input("Enter the number of your choice: ")

            if choice == '1':
                # Let the user choose another entity
                entity_number = int(input("Enter the number of the entity to examine: "))
            elif choice == '2':
                break
            else:
                print("Invalid choice. Please enter '1' or '2'.")
    else:
        print("Invalid entity number.")

def analyze_flow_method(tokenized_sentences):
    # Identify key connectors or transition words indicating flow
    connectors = ['next', 'then', 'after', 'finally', 'in conclusion', 'first', 'second', 'third']

    # Extract relationships based on connectors
    relationships = []
    for i, sentence_tokens in enumerate(tokenized_sentences):
        for connector in connectors:
            if connector in sentence_tokens:
                if i < len(tokenized_sentences) - 1:
                    relationships.append((connector, tokenized_sentences[i + 1][0]))

    if relationships:
        df = pd.DataFrame(relationships, columns=['Connector', 'Next Word'])
        plt.figure(figsize=(8, 6))
        heatmap = sns.heatmap(pd.crosstab(df['Connector'], df['Next Word']), cmap="YlGnBu", annot=True, fmt='g')
        plt.title('Flow Relationships Between Connectors and Next Words')
        plt.show()

if __name__ == "__main__":
    paragraph = """
    The flow method allows process descriptions with paragraph-like structures to describe the process, 
    presenting information in a logical order while using indentation or bullet points for delineation 
    in stages, steps, or phases of the process to the reader. The flow method can be expanded for a nest 
    of detail structure, allowing a broader context. This is useful for information with various levels 
    of granularity, and you can use indentation or bullet points to separate and distinguish anymore. 
    The flow method also permits for a project overview, presenting information cohesively, starting with 
    a general introduction and progressively delving into more specific details. This helps readers 
    follow the logical flow of ideas and gain a comprehensive understanding of the overall concept.
    """

    while True:
        # Let the user choose the analysis method
        print("\nChoose an analysis method:")
        print("1. Charting Method")
        print("2. Feature Matrix Method")
        print("3. Flow Method")
        print("4. Exit")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            analyze_paragraph_structure(paragraph, method='charting')
        elif choice == '2':
            # Let the user choose which entity to examine
            entity_number = int(input("Enter the number of the entity to examine: "))
            analyze_paragraph_structure(paragraph, method='feature_matrix', entity_number=entity_number)
        elif choice == '3':
            analyze_paragraph_structure(paragraph, method='flow')
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter '1', '2', '3', or '4'.")
