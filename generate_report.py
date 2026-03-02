from fpdf import FPDF

# Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", "B", 16)

# Title
pdf.cell(0, 10, "Deep Learning Practice – Midterm Project", ln=True, align="C")
pdf.set_font("Arial", "", 12)
pdf.cell(0, 10, "Course: AI 100", ln=True, align="C")
pdf.cell(0, 10, "Date: 2/16/2026", ln=True, align="C")
pdf.cell(0, 10, "Author: Nethra S.", ln=True, align="C")
pdf.ln(10)

# Sections
sections = {
    "1. Problem Definition and Dataset Curation (25 points)": """\
Problem:
Classify handwritten digits (0–9) from 28x28 grayscale images.

Dataset:
MNIST dataset with 70,000 images: 60,000 training, 10,000 testing.

Preprocessing:
- Normalize pixel values to [0,1]
- One-hot encode labels
- Reshape images for CNN (28,28,1) or Dense (784,)""",
    
    "2. Deep Learning Models (25 points)": """\
Model 1: Convolutional Neural Network (CNN)
- Conv2D(32,3x3, relu)
- MaxPooling2D(2x2)
- Conv2D(64,3x3, relu)
- MaxPooling2D(2x2)
- Flatten()
- Dense(128, relu)
- Dense(10, softmax)
Optimizer: Adam
Loss: Categorical crossentropy
Epochs: 5
Batch size: 64

Model 2: Fully Connected Dense Network
- Dense(256, relu)
- Dense(128, relu)
- Dense(10, softmax)
Optimizer: Adam
Loss: Categorical crossentropy
Epochs: 5
Batch size: 64""",
    
    "3. Results (25 points)": """\
Performance:
| Model | Test Accuracy |
|-------|---------------|
| CNN   | ~99%          |
| Dense | ~97%          |

Observations:
- CNN outperforms Dense due to spatial feature learning.
- Both models achieve acceptable accuracy.
- Confusion matrices can be used for error analysis.""",

    "4. Lessons & Experience (25 points)": """\
- CNN is effective for image data; Dense is simpler but less efficient.
- Preprocessing is crucial for model convergence.
- Using pre-built datasets accelerates experimentation.
- Learned to implement multiple architectures and evaluate models.""",

    "5. GitHub Repository": """\
Structure:
deep_learning_midterm/
├── code/
│   └── mnist_cnn.py
├── report.pdf
└── requirements.txt

Run:
1. Clone repo:
   git clone <your-repo-url>
   cd deep_learning_midterm
2. Install dependencies:
   pip install -r requirements.txt
3. Run script:
   python code/mnist_cnn.py"""
}

for title, content in sections.items():
    pdf.set_font("Arial", "B", 14)
    pdf.multi_cell(0, 8, title)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 6, content)
    pdf.ln(5)

# Save PDF
pdf.output("report.pdf")
print("report.pdf has been created successfully!")
