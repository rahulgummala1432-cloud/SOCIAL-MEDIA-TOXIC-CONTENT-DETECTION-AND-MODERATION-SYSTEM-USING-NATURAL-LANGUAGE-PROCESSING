"""
Social Media Toxic Content Detection System
Detects toxic, offensive, and harmful content using NLP and machine learning
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, confusion_matrix, roc_curve, auc, roc_auc_score)
import warnings
warnings.filterwarnings('ignore')

# Set style for visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

def generate_toxic_content_dataset(n_samples=1000, random_state=42):
    """Generate synthetic toxic content dataset"""
    np.random.seed(random_state)
    
    # Toxic content examples
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
    
    # Non-toxic content examples
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
        # Add some variation
        if np.random.random() > 0.5:
            phrase = phrase.upper()
        if np.random.random() > 0.7:
            phrase += "!!!"
        data.append(phrase)
        labels.append(1)  # Toxic
    
    # Generate non-toxic samples
    for _ in range(n_samples // 2):
        phrase = np.random.choice(non_toxic_phrases)
        if np.random.random() > 0.5:
            phrase = phrase.capitalize()
        if np.random.random() > 0.8:
            phrase += "."
        data.append(phrase)
        labels.append(0)  # Non-toxic
    
    df = pd.DataFrame({'content': data, 'label': labels})
    df = df.sample(frac=1, random_state=random_state).reset_index(drop=True)
    
    return df

def extract_text_features(texts):
    """Extract linguistic features from text"""
    features = []
    
    for text in texts:
        feature_dict = {
            'length': len(text),
            'word_count': len(text.split()),
            'uppercase_ratio': sum(1 for c in text if c.isupper()) / max(len(text), 1),
            'exclamation_count': text.count('!'),
            'question_count': text.count('?'),
            'punctuation_density': sum(1 for c in text if c in '!?.,:;') / max(len(text), 1),
            'has_curse_words': 1 if any(word in text.lower() for word in ['stupid', 'idiot', 'moron', 'trash']) else 0,
            'has_threats': 1 if any(word in text.lower() for word in ['kill', 'die', 'hurt', 'destroy']) else 0,
            'has_hate_speech': 1 if any(word in text.lower() for word in ['hate', 'despise', 'loathe']) else 0,
        }
        features.append(feature_dict)
    
    return pd.DataFrame(features)

def train_models(X_train, X_test, y_train, y_test):
    """Train multiple classification models"""
    models = {}
    results = {}
    
    # Model 1: Logistic Regression
    print("Training Logistic Regression...")
    lr_model = LogisticRegression(max_iter=1000, random_state=42)
    lr_model.fit(X_train, y_train)
    y_pred_lr = lr_model.predict(X_test)
    y_pred_proba_lr = lr_model.predict_proba(X_test)[:, 1]
    
    models['Logistic Regression'] = lr_model
    results['Logistic Regression'] = {
        'predictions': y_pred_lr,
        'probabilities': y_pred_proba_lr,
        'accuracy': accuracy_score(y_test, y_pred_lr),
        'precision': precision_score(y_test, y_pred_lr),
        'recall': recall_score(y_test, y_pred_lr),
        'f1': f1_score(y_test, y_pred_lr),
        'roc_auc': roc_auc_score(y_test, y_pred_proba_lr)
    }
    
    # Model 2: Random Forest
    print("Training Random Forest...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    y_pred_proba_rf = rf_model.predict_proba(X_test)[:, 1]
    
    models['Random Forest'] = rf_model
    results['Random Forest'] = {
        'predictions': y_pred_rf,
        'probabilities': y_pred_proba_rf,
        'accuracy': accuracy_score(y_test, y_pred_rf),
        'precision': precision_score(y_test, y_pred_rf),
        'recall': recall_score(y_test, y_pred_rf),
        'f1': f1_score(y_test, y_pred_rf),
        'roc_auc': roc_auc_score(y_test, y_pred_proba_rf)
    }
    
    # Model 3: Gradient Boosting
    print("Training Gradient Boosting...")
    gb_model = GradientBoostingClassifier(n_estimators=100, random_state=42)
    gb_model.fit(X_train, y_train)
    y_pred_gb = gb_model.predict(X_test)
    y_pred_proba_gb = gb_model.predict_proba(X_test)[:, 1]
    
    models['Gradient Boosting'] = gb_model
    results['Gradient Boosting'] = {
        'predictions': y_pred_gb,
        'probabilities': y_pred_proba_gb,
        'accuracy': accuracy_score(y_test, y_pred_gb),
        'precision': precision_score(y_test, y_pred_gb),
        'recall': recall_score(y_test, y_pred_gb),
        'f1': f1_score(y_test, y_pred_gb),
        'roc_auc': roc_auc_score(y_test, y_pred_proba_gb)
    }
    
    return models, results

def plot_content_distribution(df):
    """Plot distribution of toxic vs non-toxic content"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Count plot
    labels_count = df['label'].value_counts()
    colors = ['#2ecc71', '#e74c3c']
    axes[0].bar(['Non-Toxic', 'Toxic'], [labels_count[0], labels_count[1]], 
                color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[0].set_ylabel('Count', fontsize=11, fontweight='bold')
    axes[0].set_title('Distribution of Content Types', fontsize=12, fontweight='bold')
    axes[0].grid(axis='y', alpha=0.3)
    for i, v in enumerate([labels_count[0], labels_count[1]]):
        axes[0].text(i, v + 10, str(v), ha='center', fontweight='bold')
    
    # Pie chart
    axes[1].pie([labels_count[0], labels_count[1]], labels=['Non-Toxic', 'Toxic'],
                colors=colors, autopct='%1.1f%%', startangle=90, 
                textprops={'fontsize': 11, 'fontweight': 'bold'})
    axes[1].set_title('Content Type Distribution', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/toxic_content_distribution.png', dpi=300, bbox_inches='tight')
    print("Saved: toxic_content_distribution.png")
    plt.close()

def plot_model_comparison(results):
    """Compare model performance metrics"""
    models = list(results.keys())
    metrics = ['accuracy', 'precision', 'recall', 'f1', 'roc_auc']
    
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    axes = axes.flatten()
    
    for idx, metric in enumerate(metrics):
        values = [results[m][metric] for m in models]
        axes[idx].bar(models, values, color=['#3498db', '#e74c3c', '#f39c12'], 
                     alpha=0.8, edgecolor='black', linewidth=1.5)
        axes[idx].set_ylabel(metric.upper(), fontsize=11, fontweight='bold')
        axes[idx].set_title(f'{metric.upper()} Comparison', fontsize=12, fontweight='bold')
        axes[idx].set_ylim([0, 1])
        axes[idx].grid(axis='y', alpha=0.3)
        for i, v in enumerate(values):
            axes[idx].text(i, v + 0.02, f'{v:.4f}', ha='center', fontweight='bold', fontsize=9)
    
    # Remove the extra subplot
    fig.delaxes(axes[5])
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/model_performance_comparison.png', dpi=300, bbox_inches='tight')
    print("Saved: model_performance_comparison.png")
    plt.close()

def plot_confusion_matrices(results, y_test):
    """Plot confusion matrices for all models"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    
    for idx, (model_name, result) in enumerate(results.items()):
        cm = confusion_matrix(y_test, result['predictions'])
        
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx],
                   cbar=False, annot_kws={'fontsize': 12, 'fontweight': 'bold'})
        axes[idx].set_xlabel('Predicted', fontsize=11, fontweight='bold')
        axes[idx].set_ylabel('Actual', fontsize=11, fontweight='bold')
        axes[idx].set_title(f'{model_name}\nAccuracy: {result["accuracy"]:.4f}', 
                           fontsize=12, fontweight='bold')
        axes[idx].set_xticklabels(['Non-Toxic', 'Toxic'])
        axes[idx].set_yticklabels(['Non-Toxic', 'Toxic'])
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/confusion_matrices.png', dpi=300, bbox_inches='tight')
    print("Saved: confusion_matrices.png")
    plt.close()

def plot_roc_curves(results, y_test):
    """Plot ROC curves for all models"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    colors = ['#3498db', '#e74c3c', '#f39c12']
    
    for idx, (model_name, result) in enumerate(results.items()):
        fpr, tpr, _ = roc_curve(y_test, result['probabilities'])
        roc_auc = result['roc_auc']
        
        ax.plot(fpr, tpr, color=colors[idx], lw=2.5, 
               label=f'{model_name} (AUC = {roc_auc:.4f})')
    
    ax.plot([0, 1], [0, 1], 'k--', lw=2, label='Random Classifier')
    ax.set_xlabel('False Positive Rate', fontsize=11, fontweight='bold')
    ax.set_ylabel('True Positive Rate', fontsize=11, fontweight='bold')
    ax.set_title('ROC Curves - Toxic Content Detection', fontsize=12, fontweight='bold')
    ax.legend(loc='lower right', fontsize=10)
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/roc_curves.png', dpi=300, bbox_inches='tight')
    print("Saved: roc_curves.png")
    plt.close()

def plot_feature_importance(models, feature_names):
    """Plot feature importance for tree-based models"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Random Forest
    rf_importance = models['Random Forest'].feature_importances_
    rf_indices = np.argsort(rf_importance)[-10:]
    axes[0].barh(range(len(rf_indices)), rf_importance[rf_indices], 
                color='#e74c3c', alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[0].set_yticks(range(len(rf_indices)))
    axes[0].set_yticklabels([feature_names[i] for i in rf_indices], fontsize=10)
    axes[0].set_xlabel('Importance', fontsize=11, fontweight='bold')
    axes[0].set_title('Random Forest - Feature Importance', fontsize=12, fontweight='bold')
    axes[0].grid(axis='x', alpha=0.3)
    
    # Gradient Boosting
    gb_importance = models['Gradient Boosting'].feature_importances_
    gb_indices = np.argsort(gb_importance)[-10:]
    axes[1].barh(range(len(gb_indices)), gb_importance[gb_indices], 
                color='#f39c12', alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[1].set_yticks(range(len(gb_indices)))
    axes[1].set_yticklabels([feature_names[i] for i in gb_indices], fontsize=10)
    axes[1].set_xlabel('Importance', fontsize=11, fontweight='bold')
    axes[1].set_title('Gradient Boosting - Feature Importance', fontsize=12, fontweight='bold')
    axes[1].grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/feature_importance.png', dpi=300, bbox_inches='tight')
    print("Saved: feature_importance.png")
    plt.close()

def plot_text_length_distribution(df):
    """Plot text length distribution by toxicity"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    toxic_lengths = df[df['label'] == 1]['content'].str.len()
    non_toxic_lengths = df[df['label'] == 0]['content'].str.len()
    
    # Histogram
    axes[0].hist([non_toxic_lengths, toxic_lengths], bins=30, 
                label=['Non-Toxic', 'Toxic'], color=['#2ecc71', '#e74c3c'], 
                alpha=0.7, edgecolor='black')
    axes[0].set_xlabel('Content Length (characters)', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Frequency', fontsize=11, fontweight='bold')
    axes[0].set_title('Content Length Distribution', fontsize=12, fontweight='bold')
    axes[0].legend()
    axes[0].grid(axis='y', alpha=0.3)
    
    # Box plot
    axes[1].boxplot([non_toxic_lengths, toxic_lengths], labels=['Non-Toxic', 'Toxic'],
                   patch_artist=True)
    axes[1].set_ylabel('Content Length (characters)', fontsize=11, fontweight='bold')
    axes[1].set_title('Content Length Box Plot', fontsize=12, fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/text_length_distribution.png', dpi=300, bbox_inches='tight')
    print("Saved: text_length_distribution.png")
    plt.close()

def main():
    print("="*80)
    print("TOXIC CONTENT DETECTION SYSTEM - MACHINE LEARNING ANALYSIS")
    print("="*80)
    
    # Generate dataset
    print("\n[1] Generating synthetic toxic content dataset...")
    df = generate_toxic_content_dataset(n_samples=1000)
    df.to_csv('/home/ubuntu/toxic_content_data.csv', index=False)
    print(f"Dataset generated: {df.shape[0]} records")
    print(f"Toxic content: {(df['label'] == 1).sum()} samples")
    print(f"Non-toxic content: {(df['label'] == 0).sum()} samples")
    
    # Extract features
    print("\n[2] Extracting text features...")
    text_features = extract_text_features(df['content'])
    
    # Vectorize text using TF-IDF
    print("[3] Vectorizing text using TF-IDF...")
    vectorizer = TfidfVectorizer(max_features=100, ngram_range=(1, 2))
    tfidf_features = vectorizer.fit_transform(df['content']).toarray()
    
    # Combine features
    X = np.hstack([text_features.values, tfidf_features])
    y = df['label'].values
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"Training set: {X_train_scaled.shape[0]} samples, {X_train_scaled.shape[1]} features")
    print(f"Test set: {X_test_scaled.shape[0]} samples")
    
    # Train models
    print("\n[4] Training classification models...")
    models, results = train_models(X_train_scaled, X_test_scaled, y_train, y_test)
    
    # Print results
    print("\n[5] Model Performance Results:")
    print("-" * 80)
    for model_name, result in results.items():
        print(f"\n{model_name}:")
        print(f"  Accuracy:  {result['accuracy']:.6f}")
        print(f"  Precision: {result['precision']:.6f}")
        print(f"  Recall:    {result['recall']:.6f}")
        print(f"  F1-Score:  {result['f1']:.6f}")
        print(f"  ROC-AUC:   {result['roc_auc']:.6f}")
    
    # Generate visualizations
    print("\n[6] Generating visualizations...")
    plot_content_distribution(df)
    plot_model_comparison(results)
    plot_confusion_matrices(results, y_test)
    plot_roc_curves(results, y_test)
    
    feature_names = list(text_features.columns) + [f'tfidf_{i}' for i in range(100)]
    plot_feature_importance(models, feature_names)
    plot_text_length_distribution(df)
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE - All visualizations saved")
    print("="*80)

if __name__ == "__main__":
    main()
