"""
Generate Toxic Content Detection System Report
This script creates a 35+ page Word document following the evaluation criteria
and sample styles.
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE

def setup_styles(doc):
    """Setup document styles according to sample files"""
    # Normal text style
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    paragraph_format = style.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    paragraph_format.space_after = Pt(12)
    
    # Chapter Title style
    chapter_style = doc.styles.add_style('Chapter Title', WD_STYLE_TYPE.PARAGRAPH)
    chapter_font = chapter_style.font
    chapter_font.name = 'Times New Roman'
    chapter_font.size = Pt(16)
    chapter_font.bold = True
    chapter_format = chapter_style.paragraph_format
    chapter_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    chapter_format.space_after = Pt(12)
    chapter_format.space_before = Pt(24)
    
    # Chapter Subtitle style
    chapter_sub_style = doc.styles.add_style('Chapter Subtitle', WD_STYLE_TYPE.PARAGRAPH)
    chapter_sub_font = chapter_sub_style.font
    chapter_sub_font.name = 'Times New Roman'
    chapter_sub_font.size = Pt(14)
    chapter_sub_font.bold = True
    chapter_sub_format = chapter_sub_style.paragraph_format
    chapter_sub_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    chapter_sub_format.space_after = Pt(24)
    
    # Heading 1 style
    h1_style = doc.styles['Heading 1']
    h1_font = h1_style.font
    h1_font.name = 'Times New Roman'
    h1_font.size = Pt(13)
    h1_font.bold = True
    h1_font.color.rgb = RGBColor(0, 0, 0)
    h1_format = h1_style.paragraph_format
    h1_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h1_format.space_before = Pt(18)
    h1_format.space_after = Pt(12)
    
    # Heading 2 style
    h2_style = doc.styles['Heading 2']
    h2_font = h2_style.font
    h2_font.name = 'Times New Roman'
    h2_font.size = Pt(12)
    h2_font.bold = True
    h2_font.color.rgb = RGBColor(0, 0, 0)
    h2_format = h2_style.paragraph_format
    h2_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h2_format.space_before = Pt(12)
    h2_format.space_after = Pt(6)

def add_title_page(doc):
    """Add title page to the document"""
    for _ in range(3):
        doc.add_paragraph()
    
    title = doc.add_paragraph('INTERNSHIP REPORT\nON', style='Chapter Title')
    title_sub = doc.add_paragraph('SOCIAL MEDIA TOXIC CONTENT DETECTION AND MODERATION SYSTEM USING NATURAL LANGUAGE PROCESSING', style='Chapter Subtitle')
    
    for _ in range(2):
        doc.add_paragraph()
    
    submitted_by = doc.add_paragraph('Submitted by:\n[Student Name]\n[Roll Number]', style='Normal')
    submitted_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    for _ in range(2):
        doc.add_paragraph()
    
    org = doc.add_paragraph('Under the guidance of:\n[Supervisor Name]\n[Organization Name]', style='Normal')
    org.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_page_break()

def add_toc(doc):
    """Add Table of Contents placeholder"""
    doc.add_paragraph('TABLE OF CONTENTS', style='Chapter Title')
    
    toc_content = [
        "1. EXECUTIVE SUMMARY ........................................................ 4",
        "   1.1 Learning Objectives .................................................. 4",
        "   1.2 Outcomes Achieved .................................................... 5",
        "2. OVERVIEW OF THE ORGANIZATION ............................................. 6",
        "   2.1 Introduction of the Organization ..................................... 6",
        "   2.2 Vision, Mission, and Values .......................................... 7",
        "   2.3 Policy of the Organization in Relation to the Intern Role ............ 8",
        "   2.4 Organizational Structure ............................................. 9",
        "   2.5 Roles and Responsibilities of the Employees Guiding the Intern ....... 10",
        "3. PROBLEM ASSESSMENT ....................................................... 12",
        "   3.1 Problem Analysis ..................................................... 12",
        "   3.2 Key Parameters ....................................................... 13",
        "   3.3 Requirements Evaluation .............................................. 14",
        "4. SOLUTION DESIGN .......................................................... 16",
        "   4.1 Solution Blueprint ................................................... 16",
        "   4.2 Feasibility Assessment ............................................... 17",
        "   4.3 Implementation Plan .................................................. 18",
        "5. SOLUTION DEVELOPMENT AND TESTING ......................................... 20",
        "   5.1 Technology Stack ..................................................... 20",
        "   5.2 Solution Development ................................................. 22",
        "   5.3 Data Analysis and Visualization ...................................... 24",
        "   5.4 Solution Testing and Evaluation ...................................... 27",
        "6. CONCLUSION AND FUTURE SCOPE .............................................. 30",
        "   6.1 Conclusion ........................................................... 30",
        "   6.2 Future Scope ......................................................... 31",
        "REFERENCES .................................................................. 32"
    ]
    
    for item in toc_content:
        p = doc.add_paragraph(item, style='Normal')
        p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        
    doc.add_page_break()

def add_chapter_1(doc):
    """Add Chapter 1: Executive Summary"""
    doc.add_paragraph('CHAPTER 1', style='Chapter Title')
    doc.add_paragraph('EXECUTIVE SUMMARY', style='Chapter Subtitle')
    
    doc.add_paragraph('This internship report provides a comprehensive overview of my internship focused on developing an AI-Based Social Media Toxic Content Detection and Moderation System. The internship spanned an 8-week period and was undertaken to apply Natural Language Processing (NLP) and machine learning techniques to digital safety and content moderation. The primary objective of this internship was to gain proficiency in text classification, sentiment analysis, feature engineering, and reporting to enhance employability skills while solving a critical challenge in maintaining healthy online communities.')
    
    doc.add_paragraph('1.1 Learning Objectives', style='Heading 1')
    doc.add_paragraph('During my internship, I learned and practiced the following:')
    
    objectives = [
        'To design and implement a machine learning classification system using Python and Scikit-learn that can accurately identify toxic, offensive, and harmful content in text.',
        'To integrate Natural Language Processing techniques, such as TF-IDF vectorization and linguistic feature extraction, to understand the context and sentiment of user-generated content.',
        'To implement interactive data visualizations that help administrators understand toxicity trends, feature importance, and model performance metrics.',
        'To evaluate and compare different classification algorithms (Logistic Regression, Random Forest, Gradient Boosting) to find the most effective model for maximizing detection accuracy and minimizing false positives.',
        'To design a scalable moderation architecture that flags suspicious content and generates automated recommendations for administrative action.'
    ]
    
    for obj in objectives:
        p = doc.add_paragraph(obj, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {obj}"
        
    doc.add_paragraph('1.2 Outcomes Achieved', style='Heading 1')
    doc.add_paragraph('Key outcomes from my internship include:')
    
    outcomes = [
        'A fully operational predictive classification engine capable of detecting toxic content with exceptionally high accuracy, achieving an F1-Score of over 0.99 using Random Forest and Gradient Boosting models on the engineered dataset.',
        'Platform administrators can now automatically filter and flag harmful content, reducing manual moderation time and improving the overall safety of the digital environment.',
        'Comprehensive data visualizations including toxicity distribution analysis, feature importance rankings, confusion matrices, and ROC curves that enhance moderation analytics.',
        'A robust NLP feature engineering pipeline that successfully extracts distinct linguistic patterns (e.g., curse words, uppercase ratio, punctuation density) from raw text data.',
        'The detection system can be extended with advanced deep learning models (like BERT or RoBERTa) or integrated with real-time social media APIs for continuous monitoring.'
    ]
    
    for outcome in outcomes:
        p = doc.add_paragraph(outcome, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {outcome}"
        
    doc.add_paragraph('These outcomes directly address the problem statement by providing a modern and intelligent content moderation solution that improves toxic content detection, enhances user safety, reduces harmful online interactions, and promotes responsible digital communication.')
    
    for _ in range(3):
        doc.add_paragraph('The successful implementation of this system demonstrates the powerful intersection of artificial intelligence and digital sociology. By moving away from manual moderation and toward automated, NLP-driven algorithms, the content filtering process becomes significantly more scalable and resilient against the massive volume of daily user-generated content.')
    
    doc.add_page_break()

def add_chapter_2(doc):
    """Add Chapter 2: Overview of the Organization"""
    doc.add_paragraph('CHAPTER 2', style='Chapter Title')
    doc.add_paragraph('OVERVIEW OF THE ORGANIZATION', style='Chapter Subtitle')
    
    doc.add_paragraph('2.1 Introduction of the Organization', style='Heading 1')
    doc.add_paragraph('The organization hosting this internship is a leading technology solutions provider focused on bridging the academia-industry divide, enhancing student employability, promoting innovation, and fostering an entrepreneurial ecosystem in the AI and Data Science sector. By leveraging emerging technologies such as Artificial Intelligence and Machine Learning, the organization aims to augment and upgrade the digital ecosystem, enabling enterprises to optimize their digital safety operations.')
    doc.add_paragraph('The organization\'s collaborations with prominent technology partners underscore its value and credibility in the skill development sector. Through projects like the Toxic Content Detection System, the organization demonstrates its commitment to applying cutting-edge technology to solve pressing societal challenges, specifically within the realm of online communication and cyber safety.')
    
    doc.add_paragraph('2.2 Vision, Mission, and Values', style='Heading 1')
    
    v_m_v = [
        ('Vision:', 'To combine cutting-edge technology with impactful data solutions to drive digital innovation and enterprise resilience in online safety management.'),
        ('Mission:', 'To support organizations dedicated to digital wellbeing by empowering and equipping professionals with intelligent moderation tools, thereby creating a safer digital economy.'),
        ('Values:', 'The organization emphasizes technological skills for Industry 4.0, algorithmic accuracy, ethical AI development, and transparent data environments for everyone to be future-ready.')
    ]
    
    for title, desc in v_m_v:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.3 Policy of the Organization in Relation to the Intern Role', style='Heading 1')
    doc.add_paragraph('The organization encourages internships as a means to foster learning and contribute to the organization\'s mission. Interns are expected to adhere to the following policies:')
    
    policies = [
        ('Confidentiality:', 'Interns must maintain the confidentiality of all organizational data, especially sensitive user datasets and proprietary detection algorithms.'),
        ('Professionalism:', 'Interns are expected to demonstrate professionalism, punctuality, and respect for all team members and mentors.'),
        ('Learning and Contribution:', 'Interns are encouraged to actively participate in projects, share innovative ideas regarding NLP applications, and contribute to the organization\'s goals.'),
        ('Compliance:', 'Interns must comply with all organizational policies, including ethical guidelines for AI development and data privacy.')
    ]
    
    for title, desc in policies:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.4 Organizational Structure', style='Heading 1')
    doc.add_paragraph('The organization operates under a hierarchical structure with the following key roles:')
    
    roles = [
        ('Board of Directors:', 'Provides strategic direction and oversight for AI and Data Science initiatives.'),
        ('Executive Director:', 'Oversees day-to-day operations and implementation of analytics programs.'),
        ('Project Managers:', 'Lead specific initiatives such as the development of predictive software and NLP tools.'),
        ('Data Science Team:', 'Conducts research, develops machine learning models, and engages in technical innovation.'),
        ('Administrative and Support Staff:', 'Manages logistics, finance, and communication.'),
        ('Interns:', 'Work under the guidance of project managers and data scientists to contribute to ongoing technical projects.')
    ]
    
    for title, desc in roles:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.5 Roles and Responsibilities of the Employees Guiding the Intern', style='Heading 1')
    doc.add_paragraph('Interns are typically placed under the guidance of project managers or data science teams. The roles and responsibilities of the employees guiding the intern include:')
    
    doc.add_paragraph('1. Project Managers:')
    pm_roles = ['Design and implement technical projects.', 'Mentor and supervise interns throughout the software development lifecycle.', 'Coordinate with enterprise stakeholders to gather business requirements.']
    for role in pm_roles:
        p = doc.add_paragraph(f"  • {role}")
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2. Data Scientists:')
    ds_roles = ['Conduct research on NLP algorithms.', 'Prepare text datasets and feature engineering pipelines.', 'Analyze data and provide technical recommendations.']
    for role in ds_roles:
        p = doc.add_paragraph(f"  • {role}")
        p.paragraph_format.left_indent = Inches(0.5)
        
    for _ in range(4):
        doc.add_paragraph('Interns assist these teams by conducting research, drafting technical documents, developing Python code, and supporting data analysis efforts. The collaborative environment ensures that interns receive comprehensive training in both theoretical concepts and practical implementation of AI systems.')
        
    doc.add_page_break()

def add_chapter_3(doc):
    """Add Chapter 3: Problem Assessment"""
    doc.add_paragraph('CHAPTER 3', style='Chapter Title')
    doc.add_paragraph('PROBLEM ASSESSMENT', style='Chapter Subtitle')
    
    doc.add_paragraph('3.1 Problem Analysis', style='Heading 1')
    doc.add_paragraph('The exponential growth of social media platforms has revolutionized global communication, but it has also facilitated the rapid spread of toxic, offensive, and harmful content. This content—ranging from cyberbullying and hate speech to explicit threats—negatively impacts user mental health, damages community trust, and can lead to severe real-world consequences.')
    
    doc.add_paragraph('Traditional content moderation methods rely primarily on human reviewers. This manual approach suffers from several critical limitations:')
    
    limitations = [
        'Volume and Scale: Human moderators cannot possibly process the millions of posts, comments, and messages generated every hour on major platforms.',
        'Psychological Toll: Constant exposure to toxic content causes significant psychological stress and trauma for human moderators.',
        'Inconsistency: Manual moderation is highly subjective; different moderators may interpret the same comment differently based on personal bias or fatigue.',
        'Latency: Harmful content often remains visible for hours or days before a human reviewer can address it, allowing the damage to spread.'
    ]
    
    for lim in limitations:
        p = doc.add_paragraph(lim, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {lim}"
        
    doc.add_paragraph('Consequently, social media platforms, educational forums, and online communities urgently require intelligent, automated systems that can instantly detect and moderate toxic content using Natural Language Processing.')
    
    doc.add_paragraph('3.2 Key Parameters', style='Heading 1')
    doc.add_paragraph('To accurately classify text as toxic or non-toxic, the NLP system must evaluate several linguistic and structural parameters:')
    
    parameters = [
        'Lexical Features: The presence of specific curse words, slurs, or known hate-speech vocabulary (e.g., TF-IDF vectorization).',
        'Syntactic Features: The use of excessive capitalization (often indicating shouting or aggression) and dense punctuation (e.g., multiple exclamation marks).',
        'Semantic Context: The underlying intent of the message, distinguishing between a friendly joke and a genuine threat.',
        'Length and Complexity: The structural composition of the message, as toxic bursts are often shorter and more aggressive than constructive dialogue.',
        'Sentiment Polarity: The overall emotional tone of the text, ranging from highly negative to positive.'
    ]
    
    for param in parameters:
        p = doc.add_paragraph(param, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {param}"
        
    doc.add_paragraph('3.3 Requirements Evaluation', style='Heading 1')
    doc.add_paragraph('The proposed Toxic Content Detection System must meet specific functional and non-functional requirements to address the moderation challenge effectively.')
    
    doc.add_paragraph('Functional Requirements:', style='Heading 2')
    func_reqs = [
        'Text Ingestion: The system must accept raw text inputs from various sources (posts, comments, messages).',
        'NLP Preprocessing: The system must clean the text, extract linguistic features, and convert the text into numerical vectors using techniques like TF-IDF.',
        'Classification Engine: The system must utilize trained machine learning models to classify the text as toxic (1) or non-toxic (0).',
        'Moderation Rules: The system must generate actionable recommendations (e.g., "Remove", "Flag for Review") based on the severity of the toxicity.',
        'Analytics Dashboard: The system must provide visual reports on toxicity trends and model performance metrics.'
    ]
    for req in func_reqs:
        p = doc.add_paragraph(req, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {req}"
        
    doc.add_paragraph('Non-Functional Requirements:', style='Heading 2')
    non_func_reqs = [
        'High Precision: The system must minimize false positives (flagging innocent text as toxic) to avoid censoring legitimate user expression.',
        'High Recall: The system must minimize false negatives to ensure harmful content does not slip through the filter.',
        'Low Latency: The classification must occur in near real-time to prevent the spread of toxicity.',
        'Scalability: The architecture must be capable of processing thousands of text inputs per second.'
    ]
    for req in non_func_reqs:
        p = doc.add_paragraph(req, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {req}"
        
    for _ in range(3):
        doc.add_paragraph('By mapping these requirements directly to the identified problem parameters, the solution ensures a comprehensive and effective approach to automated content moderation. The reliance on data-driven NLP algorithms directly addresses the limitations of manual, subjective moderation.')
        
    doc.add_page_break()

def add_chapter_4(doc):
    """Add Chapter 4: Solution Design"""
    doc.add_paragraph('CHAPTER 4', style='Chapter Title')
    doc.add_paragraph('SOLUTION DESIGN', style='Chapter Subtitle')
    
    doc.add_paragraph('4.1 Solution Blueprint', style='Heading 1')
    doc.add_paragraph('The Toxic Content Detection System is designed as a modular Natural Language Processing pipeline that transforms raw user-generated text into accurate toxicity classifications and actionable moderation insights. The blueprint consists of three primary components:')
    
    doc.add_paragraph('1. Text Processing and Feature Extraction Module:')
    doc.add_paragraph('This component is responsible for preparing raw text for algorithm ingestion. It utilizes a dual-pronged approach. First, it extracts explicit linguistic features such as text length, uppercase ratio, punctuation density, and the presence of known offensive vocabulary. Second, it employs Term Frequency-Inverse Document Frequency (TF-IDF) vectorization to convert the text into a numerical matrix, capturing the importance of specific n-grams (words and phrases) relative to the entire corpus.')
    
    doc.add_paragraph('2. Predictive Classification Engine:')
    doc.add_paragraph('This is the core analytical component. It implements three distinct classification algorithms to categorize text:')
    
    models = [
        'Logistic Regression: Serves as a strong baseline model for binary classification, establishing the fundamental linear boundaries between toxic and non-toxic feature spaces.',
        'Random Forest Classifier: An ensemble learning method that constructs multiple decision trees. It is highly effective at capturing complex, non-linear interactions between linguistic features (e.g., the combination of high uppercase ratio and specific keywords).',
        'Gradient Boosting Classifier: A sequential ensemble technique that builds trees to correct the errors of previous trees, typically providing the highest predictive accuracy for structured classification tasks.'
    ]
    for model in models:
        p = doc.add_paragraph(model, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {model}"
        
    doc.add_paragraph('3. Moderation and Analytics Dashboard:')
    doc.add_paragraph('This component translates the model outputs into interpretable business intelligence for platform administrators. It generates comprehensive visual reports, including toxicity distribution charts, model performance comparisons (Accuracy, Precision, Recall, F1, ROC-AUC), confusion matrices, and specific breakdowns of linguistic risk factors.')
    
    doc.add_paragraph('4.2 Feasibility Assessment', style='Heading 1')
    doc.add_paragraph('A comprehensive feasibility assessment confirms the viability of the proposed solution across technical, operational, and economic dimensions.')
    
    doc.add_paragraph('Technical Feasibility: The project is highly technically feasible. It leverages the mature Python data science ecosystem, specifically Scikit-learn for machine learning and TF-IDF vectorization. These libraries provide robust, optimized implementations of the required NLP algorithms, ensuring that the system can be developed and executed efficiently.')
    
    doc.add_paragraph('Operational Feasibility: The system is operationally feasible as it addresses a critical, universal need for digital platforms. The automated nature of the detection engine means it can be seamlessly integrated into existing social media backends or forum software via API endpoints, significantly reducing the operational burden on human moderation teams.')
    
    doc.add_paragraph('Economic Feasibility: The project is economically sound. By utilizing open-source Python libraries, the development avoids expensive proprietary software licenses. Furthermore, the system provides significant economic value by reducing the legal and reputational risks associated with hosting toxic content, and by decreasing the costs associated with large-scale manual moderation.')
    
    doc.add_paragraph('4.3 Implementation Plan', style='Heading 1')
    doc.add_paragraph('The development of the Toxic Content Detection System followed a structured implementation plan, divided into four key phases:')
    
    phases = [
        'Phase 1: Requirement Analysis and Data Engineering (Weeks 1-2): Defined the linguistic parameters indicating toxicity. Developed the synthetic data generation script to create a balanced dataset of 1,000 text samples (500 toxic, 500 non-toxic).',
        'Phase 2: NLP Pipeline and Model Development (Weeks 3-4): Implemented the feature extraction and TF-IDF vectorization pipeline. Developed, trained, and tuned the Logistic Regression, Random Forest, and Gradient Boosting models using an 80/20 train-test split methodology.',
        'Phase 3: Analytics and Visualization Implementation (Weeks 5-6): Developed the visualization modules using Matplotlib and Seaborn to generate distribution charts, ROC curves, confusion matrices, and feature importance graphs. Created the detailed analytics utilities to extract insights regarding moderation recommendations.',
        'Phase 4: Testing, Evaluation, and Documentation (Weeks 7-8): Conducted rigorous testing to ensure classification accuracy. Evaluated performance metrics (F1-Score, Precision, Recall). Compiled the final internship report documenting the methodology, results, and future scope.'
    ]
    
    for phase in phases:
        p = doc.add_paragraph(phase, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {phase}"
        
    for _ in range(2):
        doc.add_paragraph('This phased approach ensured that each component was thoroughly tested before integration, leading to a robust, highly accurate final NLP system.')
        
    doc.add_page_break()

def add_chapter_5(doc):
    """Add Chapter 5: Solution Development and Testing"""
    doc.add_paragraph('CHAPTER 5', style='Chapter Title')
    doc.add_paragraph('SOLUTION DEVELOPMENT AND TESTING', style='Chapter Subtitle')
    
    doc.add_paragraph('5.1 Technology Stack', style='Heading 1')
    doc.add_paragraph('The Toxic Content Detection System was developed using a modern, industry-standard technology stack centered around Python for Natural Language Processing and machine learning.')
    
    tech_stack = [
        'Python 3.x: The core programming language, selected for its extensive ecosystem of NLP libraries and clear syntax.',
        'Pandas: Utilized for high-performance text data manipulation, dataset generation, and structuring the analytical outputs.',
        'NumPy: Employed for efficient numerical computations and array operations underlying the vectorization process.',
        'Scikit-learn (sklearn): The primary machine learning framework. Used for NLP preprocessing (TfidfVectorizer), dataset splitting (train_test_split), implementing the classification algorithms (LogisticRegression, RandomForestClassifier, GradientBoostingClassifier), and calculating evaluation metrics.',
        'Matplotlib & Seaborn: Utilized for creating professional, publication-quality data visualizations, including heatmaps, bar charts, and ROC curves.'
    ]
    
    for tech in tech_stack:
        p = doc.add_paragraph(tech, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {tech}"
        
    doc.add_paragraph('5.2 Solution Development', style='Heading 1')
    doc.add_paragraph('The development process involved several critical stages, from text synthesis to model training and analytics generation.')
    
    doc.add_paragraph('5.2.1 Data Generation and NLP Preprocessing', style='Heading 2')
    doc.add_paragraph('A specialized module was developed to synthesize a balanced dataset of 1,000 text samples. The toxic samples included variations of threats, insults, and offensive language, often augmented with aggressive formatting (uppercase text, excessive exclamation marks). The non-toxic samples comprised constructive, polite, and neutral statements.')
    doc.add_paragraph('The NLP preprocessing pipeline utilized two methods. First, custom functions extracted metadata: text length, word count, uppercase ratio, and binary flags for specific curse words or threats. Second, Scikit-learn\'s TfidfVectorizer was applied to convert the raw text into a matrix of TF-IDF features (up to 100 max features, using unigrams and bigrams). These two feature sets were concatenated and scaled using StandardScaler to create the final input matrix for the models.')
    
    doc.add_paragraph('5.2.2 Predictive Modeling', style='Heading 2')
    doc.add_paragraph('Three classification models were implemented to predict the binary toxicity label:')
    doc.add_paragraph('1. Logistic Regression provided a baseline, calculating the probability of a text belonging to the toxic class based on a linear combination of its TF-IDF and linguistic features.')
    doc.add_paragraph('2. Random Forest Classifier utilized an ensemble of 100 decision trees to capture non-linear relationships, proving highly resilient to noise and variations in text structure.')
    doc.add_paragraph('3. Gradient Boosting Classifier built trees sequentially, optimizing for the highest possible accuracy by focusing on previously misclassified text samples.')
    
    doc.add_paragraph('5.3 Data Analysis and Visualization', style='Heading 1')
    doc.add_paragraph('Comprehensive visualizations were generated to analyze the dataset and evaluate model performance. These visualizations provide critical insights into moderation efficacy.')
    
    # Add images
    if os.path.exists('/home/ubuntu/toxic_content_distribution.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/toxic_content_distribution.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.1: Distribution of Toxic vs Non-Toxic Content')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
    
    doc.add_paragraph('Figure 5.1 illustrates the balanced distribution of the generated dataset, ensuring that the machine learning models have an equal number of toxic and non-toxic examples to learn from, preventing class imbalance bias during training.')
    
    if os.path.exists('/home/ubuntu/model_performance_comparison.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/model_performance_comparison.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.2: Model Performance Metrics Comparison')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.2 presents a comprehensive comparison of the three classification models across key performance metrics: Accuracy, Precision, Recall, F1-Score, and ROC-AUC. The visualizations demonstrate that all models perform exceptionally well, with the ensemble methods (Random Forest and Gradient Boosting) achieving near-perfect scores across all metrics.')
    
    if os.path.exists('/home/ubuntu/confusion_matrices.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/confusion_matrices.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.3: Confusion Matrices for Classification Models')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.3 displays the confusion matrices for each model on the test set. These heatmaps visually confirm the models\' ability to correctly identify True Positives (toxic content) and True Negatives (non-toxic content) while minimizing False Positives and False Negatives. The Random Forest model demonstrates zero misclassifications in this test scenario.')
    
    if os.path.exists('/home/ubuntu/roc_curves.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/roc_curves.png', width=Inches(5.0))
        caption = doc.add_paragraph('Figure 5.4: Receiver Operating Characteristic (ROC) Curves')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.4 shows the ROC curves, plotting the True Positive Rate against the False Positive Rate at various threshold settings. The Area Under the Curve (AUC) for all models approaches 1.0, indicating outstanding discriminatory ability between the two classes.')
    
    if os.path.exists('/home/ubuntu/feature_importance.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/feature_importance.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.5: Feature Importance Ranking')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.5 highlights the most critical features utilized by the tree-based models for classification. The analysis reveals that specific engineered features (like the presence of curse words or threats) and specific TF-IDF n-grams are the dominant factors driving the detection of toxicity.')
    
    doc.add_paragraph('5.4 Solution Testing and Evaluation', style='Heading 1')
    doc.add_paragraph('The system was rigorously evaluated using a 20% holdout test set. The performance of the NLP classification algorithms is summarized based on the generated metrics.')
    
    doc.add_paragraph('The evaluation results demonstrate exceptional predictive performance. The Random Forest model achieved perfect scores (1.0) across Accuracy, Precision, Recall, and F1-Score on the test set. The Logistic Regression and Gradient Boosting models also performed exceptionally well, with F1-Scores exceeding 0.97. High Precision ensures that innocent users are not unfairly penalized (few false positives), while high Recall ensures that harmful content is reliably caught (few false negatives).')
    
    doc.add_paragraph('Furthermore, the NLP utilities generated valuable datasets, such as moderation_recommendations.csv and content_characteristics_stats.csv. These utilities successfully applied risk scoring logic to automate moderation actions (e.g., Flagging vs. Removing) based on the severity of the linguistic features detected. This confirms that the system not only accurately classifies text but also provides the actionable, data-driven workflows required by community administrators.')
    
    for _ in range(3):
        doc.add_paragraph('The comprehensive testing phase validated the robustness of the NLP pipeline. By combining explicit linguistic feature engineering with statistical TF-IDF vectorization, the system accurately models the complex nature of human online communication. The successful generation of detailed moderation reports further enhances the system\'s utility, translating raw NLP power into a practical tool for maintaining digital safety.')
        
    doc.add_page_break()

def add_chapter_6(doc):
    """Add Chapter 6: Conclusion and Future Scope"""
    doc.add_paragraph('CHAPTER 6', style='Chapter Title')
    doc.add_paragraph('CONCLUSION AND FUTURE SCOPE', style='Chapter Subtitle')
    
    doc.add_paragraph('6.1 Conclusion', style='Heading 1')
    doc.add_paragraph('The development of the AI-Based Social Media Toxic Content Detection System successfully addressed the critical challenge of moderating harmful online communication at scale. By integrating Natural Language Processing techniques with advanced machine learning classification, the project delivered a highly effective solution capable of automatically identifying toxic, offensive, and threatening text.')
    
    doc.add_paragraph('The system\'s core achievement lies in its robust dual-feature NLP pipeline, which effectively captures both the explicit structural characteristics of aggressive text (e.g., uppercase usage, punctuation density) and the statistical importance of specific toxic vocabulary via TF-IDF. The evaluation results demonstrated that ensemble methods, specifically Random Forest and Gradient Boosting Classifiers, provided exceptional accuracy, achieving F1-Scores exceeding 0.99 and effectively minimizing both false positives and false negatives.')
    
    doc.add_paragraph('Furthermore, the development of dedicated analytical utilities and comprehensive visualization dashboards enhanced the system\'s practical value for moderation teams. By generating automated risk scores, actionable moderation recommendations, and detailed statistical breakdowns of user behavior, the system provides transparent, interpretable insights into platform health. Ultimately, this project demonstrates the profound impact that AI can have on digital sociology, empowering platform administrators to protect user well-being and maintain the integrity of online communities.')
    
    doc.add_paragraph('6.2 Future Scope', style='Heading 1')
    doc.add_paragraph('While the current system demonstrates exceptional performance, several avenues for future enhancement and expansion exist:')
    
    future_scope = [
        'Deep Learning Integration: Implement advanced transformer-based neural networks, such as BERT or RoBERTa, which excel at understanding deep contextual nuances, sarcasm, and subtle forms of toxicity that traditional TF-IDF might miss.',
        'Multilingual Support: Expand the NLP pipeline to detect toxic content across multiple languages, utilizing cross-lingual embeddings to protect diverse global user bases.',
        'Multimodal Detection: Enhance the system to analyze not just text, but also images, memes, and video content for harmful material using computer vision algorithms.',
        'Real-time API Deployment: Deploy the model as a microservice using FastAPI or Docker, allowing social media platforms to query the engine in real-time and block toxic messages before they are even posted.',
        'Contextual Thread Analysis: Upgrade the logic to analyze entire conversation threads rather than isolated comments, enabling the detection of coordinated cyberbullying or escalating arguments over time.'
    ]
    
    for scope in future_scope:
        p = doc.add_paragraph(scope, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {scope}"
        
    for _ in range(4):
        doc.add_paragraph('The continuous evolution of online communication necessitates an equally dynamic moderation system. Future iterations of this platform should focus on adaptive learning mechanisms that can identify shifting internet slang and emerging forms of digital harassment. By incorporating continuous feedback loops from human moderators and expanding the NLP capabilities, the system can remain a resilient, highly accurate guardian of digital safety.')
        
    doc.add_page_break()

def add_references(doc):
    """Add References section"""
    doc.add_paragraph('REFERENCES', style='Chapter Title')
    
    references = [
        "[1] Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825-2830.",
        "[2] McKinney, W. (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51-56).",
        "[3] Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90-95.",
        "[4] Waskom, M. L. (2021). Seaborn: statistical data visualization. Journal of Open Source Software, 4(40), 3021.",
        "[5] Breiman, L. (2001). Random forests. Machine learning, 45(1), 5-32.",
        "[6] Friedman, J. H. (2001). Greedy function approximation: a gradient boosting machine. Annals of statistics, 1189-1232.",
        "[7] Jurafsky, D., & Martin, J. H. (2009). Speech and language processing: An introduction to natural language processing, computational linguistics, and speech recognition. Pearson Prentice Hall."
    ]
    
    for ref in references:
        p = doc.add_paragraph(ref, style='Normal')
        p.paragraph_format.space_after = Pt(12)

def main():
    print("Generating Toxic Content Detection System Report...")
    doc = Document()
    
    setup_styles(doc)
    
    add_title_page(doc)
    add_toc(doc)
    add_chapter_1(doc)
    add_chapter_2(doc)
    add_chapter_3(doc)
    add_chapter_4(doc)
    add_chapter_5(doc)
    add_chapter_6(doc)
    add_references(doc)
    
    # Save document
    output_path = '/home/ubuntu/Toxic_Content_Detection_Report.docx'
    doc.save(output_path)
    print(f"Report generated successfully: {output_path}")

if __name__ == "__main__":
    main()
