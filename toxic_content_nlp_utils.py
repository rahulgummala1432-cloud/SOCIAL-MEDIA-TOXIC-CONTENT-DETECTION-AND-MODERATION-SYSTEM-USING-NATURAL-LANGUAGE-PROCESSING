"""
NLP Utilities for Toxic Content Detection
Generates detailed analytical datasets and insights for content moderation
"""

import numpy as np
import pandas as pd
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

def generate_toxic_content_dataset(n_samples=1000, random_state=42):
    """Generate synthetic toxic content dataset"""
    np.random.seed(random_state)
    
    toxic_phrases = [
        "you are so stupid", "i hate you", "kill yourself", "you suck",
        "go die", "you're worthless", "nobody likes you", "you're disgusting",
        "i hope you die", "you're a loser", "you're pathetic", "shut up idiot",
        "you deserve to die", "you're trash", "go away you moron", "you're ugly",
        "you're a waste of space", "everyone hates you", "you're a failure",
        "you're disgusting", "i wish you were dead", "you're so annoying",
        "you're a piece of garbage", "you're worthless scum", "you're evil",
        "you're a monster", "you deserve pain", "you're subhuman", "you're filth"
    ]
    
    non_toxic_phrases = [
        "have a great day", "thanks for sharing", "i appreciate your help",
        "that's a good point", "i agree with you", "nice work on that",
        "you did well", "i like your idea", "that's helpful", "thanks for the update",
        "good morning everyone", "hope you're doing well", "thanks for the feedback",
        "great job on the project", "i enjoyed reading that", "thanks for your support",
        "that's interesting", "i learned something new", "appreciate your perspective",
        "thanks for being there", "you're a good friend", "i'm proud of you",
        "that's wonderful news", "congratulations on your success", "you inspire me",
        "thanks for everything", "you're amazing", "keep up the good work"
    ]
    
    data = []
    labels = []
    
    # Generate toxic samples
    for _ in range(n_samples // 2):
        phrase = np.random.choice(toxic_phrases)
        if np.random.random() > 0.5:
            phrase = phrase.upper()
        if np.random.random() > 0.7:
            phrase += "!!!"
        data.append(phrase)
        labels.append(1)
    
    # Generate non-toxic samples
    for _ in range(n_samples // 2):
        phrase = np.random.choice(non_toxic_phrases)
        if np.random.random() > 0.5:
            phrase = phrase.capitalize()
        if np.random.random() > 0.8:
            phrase += "."
        data.append(phrase)
        labels.append(0)
    
    df = pd.DataFrame({'content': data, 'label': labels})
    df = df.sample(frac=1, random_state=random_state).reset_index(drop=True)
    
    return df

def analyze_content_characteristics(df):
    """Analyze characteristics of toxic vs non-toxic content"""
    print("[1] Analyzing content characteristics...")
    
    stats = []
    for label, label_name in [(0, 'Non-Toxic'), (1, 'Toxic')]:
        subset = df[df['label'] == label]['content']
        
        lengths = subset.str.len()
        word_counts = subset.str.split().str.len()
        uppercase_ratios = subset.apply(lambda x: sum(1 for c in x if c.isupper()) / max(len(x), 1))
        
        stats.append({
            'Content_Type': label_name,
            'Count': len(subset),
            'Avg_Length': lengths.mean(),
            'Avg_Words': word_counts.mean(),
            'Avg_Uppercase_Ratio': uppercase_ratios.mean(),
            'Min_Length': lengths.min(),
            'Max_Length': lengths.max(),
            'Std_Length': lengths.std()
        })
    
    stats_df = pd.DataFrame(stats)
    stats_df.to_csv('/home/ubuntu/content_characteristics_stats.csv', index=False)
    print("✓ Saved: content_characteristics_stats.csv")
    return stats_df

def analyze_toxicity_patterns(df):
    """Analyze patterns in toxic content"""
    print("[2] Analyzing toxicity patterns...")
    
    toxic_content = df[df['label'] == 1]['content'].str.lower()
    non_toxic_content = df[df['label'] == 0]['content'].str.lower()
    
    # Common words in toxic content
    toxic_words = []
    for text in toxic_content:
        toxic_words.extend(text.split())
    
    toxic_word_freq = Counter(toxic_words).most_common(20)
    
    # Common words in non-toxic content
    non_toxic_words = []
    for text in non_toxic_content:
        non_toxic_words.extend(text.split())
    
    non_toxic_word_freq = Counter(non_toxic_words).most_common(20)
    
    patterns = []
    
    # Toxic patterns
    for word, count in toxic_word_freq:
        patterns.append({
            'Type': 'Toxic',
            'Pattern': word,
            'Frequency': count,
            'Percentage': (count / len(toxic_words)) * 100
        })
    
    # Non-toxic patterns
    for word, count in non_toxic_word_freq:
        patterns.append({
            'Type': 'Non-Toxic',
            'Pattern': word,
            'Frequency': count,
            'Percentage': (count / len(non_toxic_words)) * 100
        })
    
    patterns_df = pd.DataFrame(patterns)
    patterns_df.to_csv('/home/ubuntu/toxicity_patterns.csv', index=False)
    print("✓ Saved: toxicity_patterns.csv")
    return patterns_df

def analyze_linguistic_features(df):
    """Analyze linguistic features of content"""
    print("[3] Analyzing linguistic features...")
    
    features_list = []
    
    for idx, row in df.iterrows():
        text = row['content']
        
        feature_dict = {
            'Content_ID': idx,
            'Label': 'Toxic' if row['label'] == 1 else 'Non-Toxic',
            'Length': len(text),
            'Word_Count': len(text.split()),
            'Uppercase_Count': sum(1 for c in text if c.isupper()),
            'Uppercase_Ratio': sum(1 for c in text if c.isupper()) / max(len(text), 1),
            'Exclamation_Marks': text.count('!'),
            'Question_Marks': text.count('?'),
            'Punctuation_Density': sum(1 for c in text if c in '!?.,:;') / max(len(text), 1),
            'Has_Curse_Words': 1 if any(word in text.lower() for word in ['stupid', 'idiot', 'moron', 'trash']) else 0,
            'Has_Threats': 1 if any(word in text.lower() for word in ['kill', 'die', 'hurt', 'destroy']) else 0,
            'Has_Hate_Speech': 1 if any(word in text.lower() for word in ['hate', 'despise', 'loathe']) else 0
        }
        features_list.append(feature_dict)
    
    features_df = pd.DataFrame(features_list)
    features_df.to_csv('/home/ubuntu/linguistic_features.csv', index=False)
    print("✓ Saved: linguistic_features.csv")
    return features_df

def generate_moderation_recommendations(df):
    """Generate moderation recommendations based on content analysis"""
    print("[4] Generating moderation recommendations...")
    
    recommendations = []
    
    for idx, row in df.iterrows():
        text = row['content']
        label = row['label']
        
        risk_score = 0
        risk_factors = []
        
        # Check for uppercase usage
        uppercase_ratio = sum(1 for c in text if c.isupper()) / max(len(text), 1)
        if uppercase_ratio > 0.3:
            risk_score += 20
            risk_factors.append('Excessive uppercase')
        
        # Check for excessive punctuation
        punct_count = text.count('!') + text.count('?')
        if punct_count > 2:
            risk_score += 15
            risk_factors.append('Excessive punctuation')
        
        # Check for curse words
        if any(word in text.lower() for word in ['stupid', 'idiot', 'moron', 'trash']):
            risk_score += 30
            risk_factors.append('Curse words detected')
        
        # Check for threats
        if any(word in text.lower() for word in ['kill', 'die', 'hurt', 'destroy']):
            risk_score += 40
            risk_factors.append('Threats detected')
        
        # Check for hate speech
        if any(word in text.lower() for word in ['hate', 'despise', 'loathe']):
            risk_score += 35
            risk_factors.append('Hate speech detected')
        
        # Determine action
        if risk_score >= 50:
            action = 'Remove Content'
            priority = 'High'
        elif risk_score >= 30:
            action = 'Flag for Review'
            priority = 'Medium'
        else:
            action = 'Approve'
            priority = 'Low'
        
        recommendations.append({
            'Content_ID': idx,
            'Content': text[:50] + '...' if len(text) > 50 else text,
            'Actual_Label': 'Toxic' if label == 1 else 'Non-Toxic',
            'Risk_Score': risk_score,
            'Risk_Factors': '; '.join(risk_factors) if risk_factors else 'None',
            'Recommended_Action': action,
            'Priority': priority
        })
    
    rec_df = pd.DataFrame(recommendations)
    rec_df.to_csv('/home/ubuntu/moderation_recommendations.csv', index=False)
    print("✓ Saved: moderation_recommendations.csv")
    return rec_df

def generate_content_insights(df):
    """Generate key insights about content data"""
    print("[5] Generating content insights...")
    
    insights = []
    
    # Overall statistics
    insights.append(f"Total Content Items: {len(df)}")
    insights.append(f"Toxic Content: {(df['label'] == 1).sum()} ({(df['label'] == 1).sum() / len(df) * 100:.1f}%)")
    insights.append(f"Non-Toxic Content: {(df['label'] == 0).sum()} ({(df['label'] == 0).sum() / len(df) * 100:.1f}%)")
    
    # Length analysis
    toxic_lengths = df[df['label'] == 1]['content'].str.len()
    non_toxic_lengths = df[df['label'] == 0]['content'].str.len()
    
    insights.append(f"\nAverage toxic content length: {toxic_lengths.mean():.1f} characters")
    insights.append(f"Average non-toxic content length: {non_toxic_lengths.mean():.1f} characters")
    
    # Linguistic patterns
    toxic_content = df[df['label'] == 1]['content'].str.lower()
    curse_words_count = sum(1 for text in toxic_content if any(word in text for word in ['stupid', 'idiot', 'moron']))
    threats_count = sum(1 for text in toxic_content if any(word in text for word in ['kill', 'die', 'hurt']))
    
    insights.append(f"\nToxic content with curse words: {curse_words_count} ({curse_words_count / (df['label'] == 1).sum() * 100:.1f}%)")
    insights.append(f"Toxic content with threats: {threats_count} ({threats_count / (df['label'] == 1).sum() * 100:.1f}%)")
    
    # Uppercase usage
    toxic_uppercase = df[df['label'] == 1]['content'].apply(lambda x: sum(1 for c in x if c.isupper()) / max(len(x), 1))
    non_toxic_uppercase = df[df['label'] == 0]['content'].apply(lambda x: sum(1 for c in x if c.isupper()) / max(len(x), 1))
    
    insights.append(f"\nAverage uppercase ratio in toxic content: {toxic_uppercase.mean():.2%}")
    insights.append(f"Average uppercase ratio in non-toxic content: {non_toxic_uppercase.mean():.2%}")
    
    # Write insights to file
    with open('/home/ubuntu/content_insights.txt', 'w') as f:
        f.write("TOXIC CONTENT DETECTION SYSTEM - KEY INSIGHTS\n")
        f.write("="*60 + "\n\n")
        for insight in insights:
            f.write(insight + "\n")
    
    print("✓ Saved: content_insights.txt")
    return insights

def generate_moderation_statistics(df):
    """Generate moderation statistics"""
    print("[6] Generating moderation statistics...")
    
    stats = []
    
    # Content type distribution
    stats.append({
        'Metric': 'Toxic Content',
        'Value': (df['label'] == 1).sum(),
        'Percentage': f"{(df['label'] == 1).sum() / len(df) * 100:.1f}%"
    })
    
    stats.append({
        'Metric': 'Non-Toxic Content',
        'Value': (df['label'] == 0).sum(),
        'Percentage': f"{(df['label'] == 0).sum() / len(df) * 100:.1f}%"
    })
    
    # Moderation priority
    high_priority = len(df[df['label'] == 1])
    medium_priority = len(df[(df['label'] == 1) & (df['content'].str.len() > 50)])
    low_priority = len(df[df['label'] == 0])
    
    stats.append({
        'Metric': 'High Priority Items',
        'Value': high_priority,
        'Percentage': f"{high_priority / len(df) * 100:.1f}%"
    })
    
    stats.append({
        'Metric': 'Medium Priority Items',
        'Value': medium_priority,
        'Percentage': f"{medium_priority / len(df) * 100:.1f}%"
    })
    
    stats.append({
        'Metric': 'Low Priority Items',
        'Value': low_priority,
        'Percentage': f"{low_priority / len(df) * 100:.1f}%"
    })
    
    stats_df = pd.DataFrame(stats)
    stats_df.to_csv('/home/ubuntu/moderation_statistics.csv', index=False)
    print("✓ Saved: moderation_statistics.csv")
    return stats_df

def main():
    print("="*80)
    print("TOXIC CONTENT NLP UTILITIES - GENERATING DETAILED DATASETS")
    print("="*80)
    print()
    
    # Generate main dataset
    print("Generating toxic content dataset...")
    df = generate_toxic_content_dataset(n_samples=1000)
    print(f"✓ Dataset created: {df.shape[0]} records\n")
    
    # Generate analytical datasets
    analyze_content_characteristics(df)
    analyze_toxicity_patterns(df)
    analyze_linguistic_features(df)
    generate_moderation_recommendations(df)
    generate_content_insights(df)
    generate_moderation_statistics(df)
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE - All datasets generated successfully")
    print("="*80)

if __name__ == "__main__":
    main()
