import pandas as pd
import matplotlib.pyplot as plt

# Load preprocessed data from CSV file
data = pd.read_csv('data/limited_cleaned_posts.csv')

# Count tag occurrences
tag_counts = data['Tags'].str.split().explode().value_counts()

# Move 'pytorch' to the top
if '<pytorch>' in tag_counts:
    tag_counts = pd.concat([pd.Series({'pytorch': tag_counts['<pytorch>']}), tag_counts.drop('<pytorch>')])

# Create table of tag counts
tag_counts_table = pd.DataFrame({'Tag': tag_counts.index, 'Count': tag_counts.values})
tag_counts_table.index.name = 'Rank'
tag_counts_table.to_csv('results/limited_tag_counts.csv')

# Create pie chart of top 20 tag counts
top_tags = tag_counts[:20]
fig, ax = plt.subplots()
ax.pie(top_tags, labels=top_tags.index, startangle=90, counterclock=False, autopct='%1.1f%%')
ax.set_title('Tag Distribution (Top 20)')
plt.savefig('results/limited_tag_distribution.png', dpi=300, bbox_inches='tight')