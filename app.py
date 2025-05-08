import streamlit as st
import pandas as pd
import numpy as np
import time
import random
from PIL import Image
import base64
import matplotlib.pyplot as plt
import altair as alt

# Set page configuration
st.set_page_config(
    page_title="BioForge Agents Interactive",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS for retro gaming aesthetic
def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=VT323&family=Space+Mono&display=swap');
        
        /* Main container */
        .main {
            background-color: #0a0a23;
            color: #ffffff;
        }
        
        /* Headers */
        h1, h2, h3 {
            font-family: 'VT323', monospace;
            color: #FFD700;
            text-shadow: 3px 3px 0px #FF4500;
            letter-spacing: 2px;
        }
        
        /* Paragraph text */
        p, li, div {
            font-family: 'Space Mono', monospace;
            color: #ffffff;
        }
        
        /* Button styling */
        .stButton > button {
            font-family: 'VT323', monospace;
            font-size: 20px;
            border: 3px solid #FFD700;
            border-radius: 0px;
            box-shadow: 3px 3px 0px #FF4500;
            background-color: #000;
            color: #FFD700;
            transition: all 0.1s;
        }
        
        .stButton > button:hover {
            background-color: #FFD700;
            color: #000;
            transform: translate(2px, 2px);
            box-shadow: 1px 1px 0px #FF4500;
        }
        
        /* Select box styling */
        .stSelectbox > div > div {
            background-color: #000;
            border: 3px solid #FFD700;
            border-radius: 0px;
            color: #FFD700;
            font-family: 'Space Mono', monospace;
        }
        
        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: #0a0a23;
            background-image: linear-gradient(0deg, #0a0a23 0%, #1a1a3a 100%);
            border-right: 3px solid #FFD700;
        }
        
        /* Pixel-perfect containers */
        .pixel-box {
            border: 3px solid #FFD700;
            background-color: #121240;
            padding: 20px;
            margin: 10px 0px;
            box-shadow: 5px 5px 0px #FF4500;
        }
        
        /* Progress bar */
        .stProgress > div > div {
            background-color: #FFD700;
        }
        
        /* Metric styling */
        .stMetric {
            background-color: #000;
            border: 2px solid #FFD700;
            padding: 10px;
            box-shadow: 3px 3px 0px #FF4500;
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: #000;
            border: 2px solid #FFD700;
            border-radius: 0px;
            color: #FFD700;
            font-family: 'VT323', monospace;
            padding: 10px 20px;
            font-size: 18px;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: #FFD700;
            color: #000;
        }
        
        /* Divider */
        hr {
            border-color: #FFD700;
            border-width: 2px;
        }
        
        /* Code blocks */
        code {
            background-color: #1e1e3f;
            color: #ff8a65;
            border: 2px solid #FFD700;
            padding: 2px 5px;
            font-family: 'Space Mono', monospace;
        }
    </style>
    """, unsafe_allow_html=True)

load_css()

# Title and introduction
def load_header():
    col1, col2 = st.columns([5, 1])
    with col1:
        st.markdown("<h1>BioForge Agents Interactive</h1>", unsafe_allow_html=True)
        st.markdown("<h3>AI-Driven Hypothesis Explorer</h3>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='font-size:60px;text-align:right'>🧬🤖</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="pixel-box">
        <p>Welcome to BioForge Agents Interactive! This platform demonstrates how a federated multi-agent AI system autonomously generates and prioritizes novel hypotheses in complex disease biology.</p>
        <p>Navigate through the different sections to explore the power of AI in accelerating biomedical discovery.</p>
    </div>
    """, unsafe_allow_html=True)

# Simulate loading animation
def loading_animation(text="PROCESSING", duration=3):
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(101):
        dots = "." * (i % 4)
        status_text.markdown(f"<p style='font-family:VT323, monospace; font-size:20px; color:#FFD700'>{text}{dots}</p>", unsafe_allow_html=True)
        progress_bar.progress(i)
        time.sleep(duration/100)
    
    status_text.empty()
    progress_bar.empty()

# Simulate pixelated data processing animation
def pixelated_processing_animation():
    st.markdown("""
    <div style="text-align:center">
        <div style="display:inline-block; width:20px; height:20px; background:#FFD700; margin:5px; animation: pulse 1s infinite alternate;"></div>
        <div style="display:inline-block; width:20px; height:20px; background:#FFD700; margin:5px; animation: pulse 1s infinite alternate 0.1s;"></div>
        <div style="display:inline-block; width:20px; height:20px; background:#FFD700; margin:5px; animation: pulse 1s infinite alternate 0.2s;"></div>
        <div style="display:inline-block; width:20px; height:20px; background:#FFD700; margin:5px; animation: pulse 1s infinite alternate 0.3s;"></div>
        <div style="display:inline-block; width:20px; height:20px; background:#FFD700; margin:5px; animation: pulse 1s infinite alternate 0.4s;"></div>
        <style>
            @keyframes pulse {
                0% { opacity: 0.3; }
                100% { opacity: 1; }
            }
        </style>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(2)

# Disease data
disease_data = {
    "Alzheimer's Disease": {
        "description": "A progressive neurologic disorder that causes brain cells to die and the brain to shrink.",
        "research_questions": [
            "Gene variants associated with early-onset Alzheimer's",
            "Role of tau protein in neurodegeneration",
            "Microbiome influence on cognitive decline",
            "Blood-brain barrier dysfunction patterns"
        ],
        "agents": {
            "Literature Mining Agent": [
                "Extracted 573 studies linking ApoE4 allele to earlier onset",
                "Identified 47 papers discussing tau protein hyperphosphorylation mechanisms",
                "Found new research suggesting gut-brain axis involvement in 128 studies"
            ],
            "Genomic Data Analysis Agent": [
                "Detected novel single nucleotide polymorphisms in TREM2 gene",
                "Identified expression patterns in 47 patients with early onset",
                "Mapped pathway interactions between APP and PSEN1/2 genes"
            ],
            "Clinical Data Integration Agent": [
                "Correlated cognitive assessment scores with biomarker presence",
                "Identified patterns in disease progression across 1,200 patient records",
                "Detected previously unknown relationship between sleep patterns and symptom severity"
            ]
        },
        "hypotheses": [
            {
                "title": "Tau Protein Misfolding Cascade Hypothesis",
                "description": "Misfolded tau proteins may trigger a cascade effect that spreads to adjacent neurons through exosome-mediated transport, potentially explaining the pattern of disease progression seen in clinical data.",
                "supporting_evidence": {
                    "Literature Mining Agent": "Multiple studies show intercellular tau protein transfer",
                    "Genomic Data Analysis Agent": "Expression changes in exosome regulatory genes correlate with disease progression",
                    "Clinical Data Integration Agent": "Disease spread patterns match predicted exosome-mediated transport routes"
                },
                "confidence": 87,
                "novelty": 72,
                "testability": 95
            },
            {
                "title": "Microglial Priming Hypothesis",
                "description": "Early-life infections may prime microglia for hyperactivation decades later, creating vulnerability to amyloid beta accumulation and neuroinflammation when triggered by age-related stressors.",
                "supporting_evidence": {
                    "Literature Mining Agent": "Studies show persistent microglial changes after infection",
                    "Genomic Data Analysis Agent": "Gene expression signatures of 'primed' microglia identified in pre-symptomatic patients",
                    "Clinical Data Integration Agent": "Statistical correlation between early-life infection history and disease onset"
                },
                "confidence": 76,
                "novelty": 88,
                "testability": 65
            },
            {
                "title": "Metabolic-Cognitive Feedback Loop Hypothesis",
                "description": "A bidirectional relationship may exist where early metabolic changes in the brain alter cognition, leading to behavior changes that further impact metabolic function, creating an accelerating disease cycle.",
                "supporting_evidence": {
                    "Literature Mining Agent": "Research shows tight coupling between brain metabolism and cognition",
                    "Genomic Data Analysis Agent": "Metabolic regulatory genes show altered expression patterns early in disease",
                    "Clinical Data Integration Agent": "Behavioral changes precede and predict metabolic biomarker shifts"
                },
                "confidence": 81,
                "novelty": 79,
                "testability": 83
            }
        ],
        "federated_improvements": [
            "Access to 50,000 additional patient records reveals stronger correlations",
            "New genomic datasets highlight previously undetected gene variants",
            "Longitudinal clinical data enables temporal validation of predicted progressions"
        ]
    },
    "Pancreatic Cancer": {
        "description": "A cancer that forms in the pancreas, a gland located behind the stomach.",
        "research_questions": [
            "Early detection biomarkers for pancreatic cancer",
            "Stromal-epithelial interactions in tumor microenvironment",
            "Immunotherapy resistance mechanisms",
            "Metabolic adaptations driving malignant transformation"
        ],
        "agents": {
            "Literature Mining Agent": [
                "Analyzed 831 papers on pancreatic tumor microenvironment",
                "Extracted data on 37 potential biomarkers from recent clinical trials",
                "Identified patterns in treatment response across 219 case studies"
            ],
            "Genomic Data Analysis Agent": [
                "Detected recurrent KRAS mutation patterns across 86 tumor samples",
                "Identified novel RNA splicing anomalies in tumor-adjacent tissues",
                "Mapped pathway alterations in tumor progression sequences"
            ],
            "Clinical Data Integration Agent": [
                "Correlated imaging features with genetic profiles across patient cohorts",
                "Identified subtle early symptoms appearing up to 18 months before diagnosis",
                "Detected patterns in treatment response based on metabolic profiles"
            ]
        },
        "hypotheses": [
            {
                "title": "Exosome-Driven Metabolic Reprogramming Hypothesis",
                "description": "Pancreatic stellate cell-derived exosomes may reprogram metabolic pathways in pre-cancerous cells, creating a permissive environment for KRAS-driven transformation through epigenetic modifications.",
                "supporting_evidence": {
                    "Literature Mining Agent": "Recent publications show exosome signaling between stellate and ductal cells",
                    "Genomic Data Analysis Agent": "Metabolic gene expression changes precede detectable KRAS mutations",
                    "Clinical Data Integration Agent": "Metabolic shifts detected in blood samples months before diagnosis"
                },
                "confidence": 78,
                "novelty": 91,
                "testability": 82
            },
            {
                "title": "Immune Exclusion Zone Hypothesis",
                "description": "Pancreatic tumors may actively construct physical and biochemical barriers that create immune 'exclusion zones,' preventing T-cell infiltration through coordinated ECM remodeling and chemokine gradient manipulation.",
                "supporting_evidence": {
                    "Literature Mining Agent": "Studies show correlation between ECM density and T-cell exclusion",
                    "Genomic Data Analysis Agent": "Expression signatures suggest coordinated ECM and chemokine regulation",
                    "Clinical Data Integration Agent": "Imaging studies reveal spatial organization of immune exclusion"
                },
                "confidence": 85,
                "novelty": 76,
                "testability": 89
            },
            {
                "title": "Metabolic-Neural Crosstalk Hypothesis",
                "description": "Pancreatic tumors may exploit neural signaling to enhance their metabolic adaptability, forming a feedback loop where metabolic stress triggers neural invasion, which then provides access to alternative metabolic substrates.",
                "supporting_evidence": {
                    "Literature Mining Agent": "Reports of neural invasion correlating with metabolic adaptation",
                    "Genomic Data Analysis Agent": "Upregulation of neurotransmitter receptors in metabolically stressed cells",
                    "Clinical Data Integration Agent": "Neural invasion patterns predict metabolic signature shifts"
                },
                "confidence": 72,
                "novelty": 94,
                "testability": 77
            }
        ],
        "federated_improvements": [
            "Access to detailed dietary records provides new environmental correlations",
            "Integration with diabetic patient monitoring data reveals early warning signs",
            "Collaborative clinical trial data enables validation of biomarker predictions"
        ]
    },
    "Type 2 Diabetes": {
        "description": "A chronic condition that affects the way the body processes blood sugar (glucose).",
        "research_questions": [
            "Beta cell dysfunction mechanisms in early disease",
            "Environmental factors affecting insulin resistance",
            "Genetic predisposition and personalized treatment approaches",
            "Neural regulation of glucose homeostasis"
        ],
        "agents": {
            "Literature Mining Agent": [
                "Analyzed 1,256 studies on beta cell functional decline",
                "Extracted patterns from 459 papers on environmental risk factors",
                "Mapped treatment efficacy data across different genetic profiles"
            ],
            "Genomic Data Analysis Agent": [
                "Identified gene variant clusters associated with treatment responsiveness",
                "Detected epigenetic patterns correlated with disease progression",
                "Mapped interconnected pathways between metabolism and inflammation"
            ],
            "Clinical Data Integration Agent": [
                "Correlated continuous glucose monitoring data with lifestyle factors",
                "Identified subtle early warning signs from electronic health records",
                "Detected patterns in drug response across diverse patient populations"
            ]
        },
        "hypotheses": [
            {
                "title": "Circadian Disruption-Metabolic Failure Hypothesis",
                "description": "Chronic disruption of circadian rhythms may trigger a progressive desynchronization of metabolic processes, leading to cellular stress that impairs beta cell function through specific epigenetic mechanisms.",
                "supporting_evidence": {
                    "Literature Mining Agent": "Multiple studies link shift work to diabetic risk",
                    "Genomic Data Analysis Agent": "Clock gene variants correlate with beta cell dysfunction patterns",
                    "Clinical Data Integration Agent": "Sleep pattern data shows strong correlation with disease progression"
                },
                "confidence": 83,
                "novelty": 76,
                "testability": 89
            },
            {
                "title": "Microbiome-Induced Metabolic Memory Hypothesis",
                "description": "Specific gut microbiome profiles may induce persistent epigenetic changes in metabolic tissues, creating a 'metabolic memory' that continues to drive insulin resistance even after the initial dysbiosis is resolved.",
                "supporting_evidence": {
                    "Literature Mining Agent": "Research shows lasting effects of temporary dysbiosis",
                    "Genomic Data Analysis Agent": "Identified stable epigenetic markers induced by microbial metabolites",
                    "Clinical Data Integration Agent": "Patient history reveals persistent effects after antibiotic treatments"
                },
                "confidence": 77,
                "novelty": 90,
                "testability": 75
            },
            {
                "title": "Neural-Metabolic Integration Failure Hypothesis",
                "description": "Dysfunction in neural circuits that monitor and regulate metabolism may precede measurable metabolic dysfunction, suggesting a central nervous system origin for what appears peripherally as insulin resistance.",
                "supporting_evidence": {
                    "Literature Mining Agent": "Studies show hypothalamic inflammation precedes peripheral insulin resistance",
                    "Genomic Data Analysis Agent": "Neural gene expression changes detected before metabolic disruption",
                    "Clinical Data Integration Agent": "Subtle autonomic nervous system dysfunction appears early in patient histories"
                },
                "confidence": 69,
                "novelty": 87,
                "testability": 72
            }
        ],
        "federated_improvements": [
            "Wearable device data provides continuous physiological monitoring insights",
            "Integration with food consumption databases reveals dietary pattern effects",
            "Cross-correlation with environmental monitoring shows pollution impact"
        ]
    }
}

# Agent icons (simple text emoji representations for the retro aesthetic)
agent_icons = {
    "Literature Mining Agent": "📚",
    "Genomic Data Analysis Agent": "🧬",
    "Clinical Data Integration Agent": "🏥"
}

# Main application
def main():
    load_header()
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Sidebar for navigation and controls
    with st.sidebar:
        st.markdown("<h2 style='text-align: center'>CONTROL PANEL</h2>", unsafe_allow_html=True)
        
        # Disease selection
        selected_disease = st.selectbox(
            "SELECT DISEASE AREA",
            list(disease_data.keys()),
            key="disease_selector"
        )
        
        # Display disease description
        st.markdown(f"""
        <div class="pixel-box">
            <p>{disease_data[selected_disease]['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Research question selection
        selected_question = st.selectbox(
            "SELECT RESEARCH QUESTION",
            disease_data[selected_disease]['research_questions'],
            key="question_selector"
        )
        
        # Federated learning toggle
        st.markdown("<h3>FEDERATION CONTROLS</h3>", unsafe_allow_html=True)
        federated_learning = st.checkbox("ENABLE FEDERATED LEARNING", value=False)
        
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("""
        <div style='text-align: center; padding: 10px;'>
            <div style='font-family: VT323, monospace; font-size: 20px; color: #FFD700;'>
                BioForge Agents v0.1
            </div>
            <div style='font-family: Space Mono, monospace; font-size: 12px; color: #FF4500;'>
                Powered by AI
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Main content area with tabs
    tab1, tab2, tab3 = st.tabs(["AGENT NETWORK", "GENERATED HYPOTHESES", "HYPOTHESIS EVALUATION"])
    
    # Tab 1: Agent Network Visualization
    with tab1:
        st.markdown("<h2>AI AGENT NETWORK</h2>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="pixel-box">
            <p>Visualizing multi-agent system processing data for: <span style='color:#FFD700'>{selected_disease}</span></p>
            <p>Research focus: <span style='color:#FF4500'>{selected_question}</span></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Agent Network Visualization
        st.markdown("""
        <div style='display: flex; justify-content: center; margin-bottom: 20px;'>
            <div style='text-align: center; position: relative;'>
                <div style='
                    width: 100px;
                    height: 100px;
                    background-color: #000;
                    border: 3px solid #FFD700;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0 auto;
                    font-family: VT323, monospace;
                    font-size: 40px;
                    color: #FFD700;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    box-shadow: 5px 5px 0px #FF4500;
                    z-index: 10;
                '>
                    🧠
                </div>
                
                <div style='
                    width: 500px;
                    height: 300px;
                    position: relative;
                '>
                    <!-- Literature Mining Agent -->
                    <div style='
                        width: 80px;
                        height: 80px;
                        background-color: #000;
                        border: 3px solid #FFD700;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-family: VT323, monospace;
                        font-size: 30px;
                        color: #FFD700;
                        position: absolute;
                        top: 20px;
                        left: 30px;
                        box-shadow: 3px 3px 0px #FF4500;
                    '>
                        📚
                    </div>
                    <div style='
                        width: 150px;
                        position: absolute;
                        top: 35px;
                        left: 120px;
                        font-family: Space Mono, monospace;
                        font-size: 12px;
                        color: #FFD700;
                    '>
                        Literature Mining Agent
                    </div>
                    
                    <!-- Genomic Agent -->
                    <div style='
                        width: 80px;
                        height: 80px;
                        background-color: #000;
                        border: 3px solid #FFD700;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-family: VT323, monospace;
                        font-size: 30px;
                        color: #FFD700;
                        position: absolute;
                        top: 150px;
                        left: 30px;
                        box-shadow: 3px 3px 0px #FF4500;
                    '>
                        🧬
                    </div>
                    <div style='
                        width: 170px;
                        position: absolute;
                        top: 165px;
                        left: 120px;
                        font-family: Space Mono, monospace;
                        font-size: 12px;
                        color: #FFD700;
                    '>
                        Genomic Data Analysis Agent
                    </div>
                    
                    <!-- Clinical Agent -->
                    <div style='
                        width: 80px;
                        height: 80px;
                        background-color: #000;
                        border: 3px solid #FFD700;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-family: VT323, monospace;
                        font-size: 30px;
                        color: #FFD700;
                        position: absolute;
                        top: 230px;
                        left: 200px;
                        box-shadow: 3px 3px 0px #FF4500;
                    '>
                        🏥
                    </div>
                    <div style='
                        width: 170px;
                        position: absolute;
                        top: 245px;
                        left: 290px;
                        font-family: Space Mono, monospace;
                        font-size: 12px;
                        color: #FFD700;
                    '>
                        Clinical Data Integration Agent
                    </div>
                    
                    <!-- Connector lines -->
                    <div style='
                        position: absolute;
                        top: 60px;
                        left: 120px;
                        width: 100px;
                        height: 3px;
                        background-color: #FF4500;
                        transform: rotate(30deg);
                    '></div>
                    <div style='
                        position: absolute;
                        top: 190px;
                        left: 120px;
                        width: 100px;
                        height: 3px;
                        background-color: #FF4500;
                        transform: rotate(-30deg);
                    '></div>
                    <div style='
                        position: absolute;
                        top: 270px;
                        left: 290px;
                        width: 100px;
                        height: 3px;
                        background-color: #FF4500;
                        transform: rotate(-60deg);
                    '></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Process data button
        if st.button("PROCESS DATA", key="process_data"):
            loading_animation("PROCESSING MULTI-AGENT DATA", 3)
            st.session_state.data_processed = True
        
        # Display agent findings if data processed
        if st.session_state.get('data_processed', False):
            st.markdown("<h3>AGENT FINDINGS</h3>", unsafe_allow_html=True)
            
            for agent, findings in disease_data[selected_disease]['agents'].items():
                with st.expander(f"{agent_icons[agent]} {agent}"):
                    st.markdown(f"""
                    <div class="pixel-box" style="background-color:#111;">
                        <p style="color:#FFD700;font-family:VT323, monospace;font-size:20px;">AGENT LOGS:</p>
                    """, unsafe_allow_html=True)
                    
                    for finding in findings:
                        st.markdown(f"""
                        <div style="border-left:3px solid #FF4500;padding-left:10px;margin:5px 0;font-family:'Space Mono', monospace;font-size:14px;color:#ffffff;background-color:#121240;">
                            {finding}
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    # Display a simple pixel chart for this agent
                    data = np.random.randint(1, 10, size=8)
                    fig, ax = plt.subplots(figsize=(5, 2))
                    ax.bar(range(len(data)), data, color='#FFD700', edgecolor='#FF4500', linewidth=2)
                    ax.set_facecolor('#000000')
                    fig.patch.set_facecolor('#000000')
                    ax.set_title('Activity Metrics', color='#FFD700', fontfamily='monospace')
                    ax.tick_params(colors='#FFD700')
                    ax.spines['bottom'].set_color('#FFD700')
                    ax.spines['top'].set_color('#FFD700')
                    ax.spines['left'].set_color('#FFD700')
                    ax.spines['right'].set_color('#FFD700')
                    st.pyplot(fig)
    
    # Tab 2: Generated Hypotheses
    with tab2:
        st.markdown("<h2>GENERATED HYPOTHESES</h2>", unsafe_allow_html=True)
        
        # Explanation text
        st.markdown(f"""
        <div class="pixel-box">
            <p>Based on multi-agent analysis for <span style='color:#FFD700'>{selected_disease}</span>, the system has generated the following novel hypotheses:</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Generate hypotheses button
        if st.button("GENERATE HYPOTHESES", key="generate_hypotheses"):
            pixelated_processing_animation()
            loading_animation("SYNTHESIZING HYPOTHESES", 4)
            st.session_state.hypotheses_generated = True
        
        # Display hypotheses if generated
        if st.session_state.get('hypotheses_generated', False):
            hypotheses = disease_data[selected_disease]['hypotheses']
            
            # Apply federated improvements if enabled
            if federated_learning:
                st.markdown(f"""
                <div class="pixel-box" style="border-color:#FF4500;background-color:#1a1a3a;">
                    <p style="color:#FFD700;font-family:VT323, monospace;font-size:20px;">⚡ FEDERATED LEARNING ACTIVE ⚡</p>
                    <p>Additional insights available from partner institutions:</p>
                    <ul>
                """, unsafe_allow_html=True)
                
                for improvement in disease_data[selected_disease]['federated_improvements']:
                    st.markdown(f"<li>{improvement}</li>", unsafe_allow_html=True)
                
                st.markdown("</ul></div>", unsafe_allow_html=True)
                
                # Slight boost to hypothesis scores when federated learning is on
                for i in range(len(hypotheses)):
                    hypotheses[i] = dict(hypotheses[i])  # Create a copy to avoid modifying the original
                    hypotheses[i]['confidence'] = min(100, hypotheses[i]['confidence'] + random.randint(5, 10))
                    hypotheses[i]['novelty'] = min(100, hypotheses[i]['novelty'] + random.randint(3, 8))
            
            # Display each hypothesis
            for idx, hypothesis in enumerate(hypotheses):
                with st.expander(f"HYPOTHESIS #{idx+1}: {hypothesis['title']}", expanded=(idx == 0)):
                    st.markdown(f"""
                    <div class="pixel-box" style="background-color:#121240;">
                        <p style="font-family:Space Mono, monospace; color: #ffffff;">{hypothesis['description']}</p>
                        
                        <h4 style="color:#FFD700;font-family:VT323, monospace;">SUPPORTING EVIDENCE:</h4>
                    """, unsafe_allow_html=True)
                    
                    for agent, evidence in hypothesis['supporting_evidence'].items():
                        st.markdown(f"""
                        <div style="margin:10px 0;">
                            <span style="color:#FF4500;font-family:VT323, monospace;">{agent_icons[agent]} {agent}:</span>
                            <div style="border-left:3px solid #FFD700;padding-left:10px;margin-top:5px;font-family:Space Mono, monospace;font-size:14px;color:#ffffff;background-color:#121240;">
                                {evidence}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Metrics visualization
                    st.markdown("<h4 style='color:#FFD700;font-family:VT323, monospace;'>HYPOTHESIS METRICS:</h4>", unsafe_allow_html=True)
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.markdown(f"""
                        <div style="text-align:center;border:2px solid #FFD700;padding:10px;margin:5px;background:#121240;">
                            <div style="font-family:VT323, monospace;color:#FFD700;">CONFIDENCE</div>
                            <div style="font-size:30px;font-family:VT323, monospace;color:#FF4500;">{hypothesis['confidence']}%</div>
                            <div style="width:100%;background:#333;height:10px;margin-top:5px;">
                                <div style="width:{hypothesis['confidence']}%;background:#FFD700;height:10px;"></div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown(f"""
                        <div style="text-align:center;border:2px solid #FFD700;padding:10px;margin:5px;background:#121240;">
                            <div style="font-family:VT323, monospace;color:#FFD700;">NOVELTY</div>
                            <div style="font-size:30px;font-family:VT323, monospace;color:#FF4500;">{hypothesis['novelty']}%</div>
                            <div style="width:100%;background:#333;height:10px;margin-top:5px;">
                                <div style="width:{hypothesis['novelty']}%;background:#FFD700;height:10px;"></div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col3:
                        st.markdown(f"""
                        <div style="text-align:center;border:2px solid #FFD700;padding:10px;margin:5px;background:#121240;">
                            <div style="font-family:VT323, monospace;color:#FFD700;">TESTABILITY</div>
                            <div style="font-size:30px;font-family:VT323, monospace;color:#FF4500;">{hypothesis['testability']}%</div>
                            <div style="width:100%;background:#333;height:10px;margin-top:5px;">
                                <div style="width:{hypothesis['testability']}%;background:#FFD700;height:10px;"></div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    # Quick action buttons for this hypothesis
                    col1, col2 = st.columns(2)
                    with col1:
                        st.button("FLAG AS HIGH POTENTIAL", key=f"high_potential_{idx}")
                    with col2:
                        st.button("REQUEST MORE EVIDENCE", key=f"more_evidence_{idx}")
    
    # Tab 3: Hypothesis Evaluation
    with tab3:
        st.markdown("<h2>HYPOTHESIS EVALUATION</h2>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="pixel-box">
            <p>Evaluate generated hypotheses and provide feedback to improve the AI system.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Only show if hypotheses have been generated
        if st.session_state.get('hypotheses_generated', False):
            # Hypothesis selection for detailed evaluation
            selected_hypothesis = st.selectbox(
                "SELECT HYPOTHESIS TO EVALUATE",
                [h['title'] for h in disease_data[selected_disease]['hypotheses']],
                key="hypothesis_evaluator"
            )
            
            # Get the selected hypothesis object
            hypothesis = next((h for h in disease_data[selected_disease]['hypotheses'] if h['title'] == selected_hypothesis), None)
            
            if hypothesis:
                st.markdown(f"""
                <div class="pixel-box" style="background-color:#111;">
                    <h3 style="color:#FFD700;font-family:VT323, monospace;">{hypothesis['title']}</h3>
                    <p style="font-family:Space Mono, monospace;">{hypothesis['description']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Evaluation form
                st.markdown("<h3>RESEARCHER FEEDBACK</h3>", unsafe_allow_html=True)
                
                potential_rating = st.slider(
                    "SCIENTIFIC POTENTIAL",
                    0, 100, 75,
                    step=5,
                    help="Rate the scientific potential of this hypothesis"
                )
                
                novelty_rating = st.slider(
                    "NOVELTY ASSESSMENT",
                    0, 100, 80,
                    step=5,
                    help="How novel do you consider this hypothesis?"
                )
                
                priority = st.select_slider(
                    "RESEARCH PRIORITY",
                    options=["LOW", "MEDIUM", "HIGH", "VERY HIGH"],
                    value="HIGH",
                    help="Set priority level for further investigation"
                )
                
                feedback = st.text_area(
                    "ADDITIONAL FEEDBACK",
                    height=100,
                    placeholder="Enter any additional feedback or suggestions for improvement..."
                )
                
                # Submit feedback button
                if st.button("SUBMIT EVALUATION", key="submit_evaluation"):
                    loading_animation("PROCESSING FEEDBACK", 2)
                    st.success("Evaluation submitted successfully! The AI system will incorporate your feedback.")
                    
                    # Show random improvement suggestion
                    improvements = [
                        "Consider expanding the literature search to include recent preprints",
                        "Additional clinical data could strengthen the correlation evidence",
                        "Genomic data analysis suggests investigating pathway X more closely",
                        "Similar patterns were observed in related disease models"
                    ]
                    
                    st.markdown(f"""
                    <div class="pixel-box" style="border-color:#FF4500;margin-top:20px;">
                        <h4 style="color:#FFD700;font-family:VT323, monospace;">AI SYSTEM RESPONSE:</h4>
                        <p>Based on your evaluation, the system suggests:</p>
                        <p style="color:#FFD700;font-family:Space Mono, monospace;">"{random.choice(improvements)}"</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Visualization of all hypotheses comparison
            st.markdown("<h3>HYPOTHESIS COMPARISON</h3>", unsafe_allow_html=True)
            
            # Create comparison data
            comparison_data = []
            for h in disease_data[selected_disease]['hypotheses']:
                comparison_data.append({
                    "Hypothesis": h['title'][:20] + "...",
                    "Confidence": h['confidence'],
                    "Novelty": h['novelty'],
                    "Testability": h['testability']
                })
            
            # Use Altair to create a grouped bar chart with retro styling
            chart_data = pd.DataFrame(comparison_data)
            
            # Reshape the data for Altair
            chart_data_melted = pd.melt(
                chart_data, 
                id_vars=['Hypothesis'], 
                value_vars=['Confidence', 'Novelty', 'Testability'],
                var_name='Metric', 
                value_name='Score'
            )
            
            # Create the chart
            chart = alt.Chart(chart_data_melted).mark_bar().encode(
                x=alt.X('Hypothesis:N', title=None),
                y=alt.Y('Score:Q', title='Score'),
                color=alt.Color('Metric:N', scale=alt.Scale(
                    domain=['Confidence', 'Novelty', 'Testability'],
                    range=['#FFD700', '#FF4500', '#00BFFF']
                )),
                column=alt.Column('Metric:N', title=None)
            ).properties(
                width=150,
                height=200
            ).configure_view(
                strokeWidth=0
            ).configure_axis(
                labelColor='#FFD700',
                titleColor='#FFD700',
                gridColor='#333333'
            )
            
            st.altair_chart(chart, use_container_width=True)
        else:
            st.info("Generate hypotheses first to enable evaluation features.")

if __name__ == "__main__":
    main()