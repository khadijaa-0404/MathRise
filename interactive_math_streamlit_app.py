import base64
import json
import os
from dotenv import load_dotenv
import streamlit as st
import streamlit.components.v1 as components

load_dotenv(dotenv_path="env")
load_dotenv()

st.set_page_config(
    page_title="MathRise",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

gemini_api_key = os.getenv("GOOGLE_API_KEY")

questions_bank_data = []
if os.path.exists("math366_bank.json"):
    try:
        with open("math366_bank.json", "r", encoding="utf-8") as f:
            questions_bank_data = json.load(f)
    except Exception:
        questions_bank_data = []

questions_bank_json_str = json.dumps(questions_bank_data, ensure_ascii=False)

chapter_files = [
    ("الفصل الأول", "Math366_pages_12_to_40.md"),
    ("الفصل الثاني", "Math366_Ch2.md"),
    ("الفصل الثالث", "Math366_Ch3.md"),
    ("الفصل الرابع", "Math366_Ch4.md"),
]

all_book_context = []
for ch_title, ch_file in chapter_files:
    if os.path.exists(ch_file):
        try:
            with open(ch_file, "r", encoding="utf-8") as f:
                all_book_context.append(
                    f"=== سياق {ch_title} ({ch_file}) ===\n" + f.read()
                )
        except Exception:
            pass

full_math366_context = "\n\n".join(all_book_context)
math366_context_json_str = json.dumps(
    full_math366_context, ensure_ascii=False
)

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    except Exception:
        return ""

bg_base64 = get_base64_image("bg.jpg.png")

st.markdown(
    """
<style>
    #MainMenu, header, footer { visibility: hidden !important; display: none !important; }
    .block-container {
        padding: 0rem !important;
        margin: 0rem !important;
        max-width: 100% !important;
        width: 100% !important;
    }
    .stApp {
        margin: 0 !important;
        padding: 0 !important;
    }
    iframe {
        display: block !important;
        width: 100% !important;
        height: 100vh !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

html_code = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&family=KaTeX_Math:ital,wght@1,400;1,700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>

    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Tajawal', sans-serif;
        }}

        html, body {{
            width: 100%;
            min-height: 100vh;
            overflow-y: auto;
            background-image: url("data:image/png;base64,{bg_base64}");
            background-size: cover;
            background-position: center top;
            background-repeat: no-repeat;
            display: flex;
            justify-content: center;
            padding: 30px 15px;
        }}

        .main-container {{
            width: 100%;
            max-width: 1200px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}

        .header-section {{
            text-align: center;
            margin-bottom: 15px;
        }}
        .main-title {{
            font-size: 3.5rem;
            font-weight: 800;
            color: #1E1B4B;
            margin-bottom: 5px;
            letter-spacing: 1px;
        }}
        .main-title span {{
            color: #5D45FD;
        }}
        .main-subtitle {{
            font-size: 1.2rem;
            color: #475569;
            margin-top: 3px;
        }}
        .divider {{
            width: 80px;
            height: 4px;
            background: #5D45FD;
            margin: 15px auto;
            border-radius: 10px;
        }}
        .choose-text {{
            font-weight: 700;
            color: #1E1B4B;
            font-size: 1.1rem;
        }}

        .stages-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
            margin-bottom: 20px;
            align-items: center;
        }}

        .stage-card {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(5px);
            border-radius: 24px;
            padding: 24px 20px;
            border: 2px solid rgba(226, 232, 240, 0.8);
            box-shadow: 0 8px 25px rgba(0,0,0,0.03);
            transition: all 0.3s ease;
            display: flex;
            flex-direction: row;
            align-items: center;
            gap: 18px;
        }}
        .stage-card:hover {{
            transform: translateY(-6px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.08);
        }}

        .stage-card.green {{ border-color: #A7F3D0; }}
        .stage-card.blue {{ border-color: #BFDBFE; }}
        .stage-card.purple {{ border-color: #E9D5FF; }}

        .icon-circle {{
            width: 90px;
            height: 90px;
            min-width: 90px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s ease;
        }}
        .stage-card:hover .icon-circle {{ transform: scale(1.05); }}

        .icon-circle.green {{ background-color: #DCFCE7; color: #16A34A; }}
        .icon-circle.blue {{ background-color: #E0F2FE; color: #0284C7; }}
        .icon-circle.purple {{ background-color: #F3E8FF; color: #9333EA; }}

        .book-icon {{ font-size: 2.7rem; }}

        .card-content {{
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            text-align: right;
            flex: 1;
        }}

        .stage-title {{
            font-size: 1.5rem;
            font-weight: 800;
            margin-bottom: 4px;
        }}
        .stage-title.green {{ color: #15803D; }}
        .stage-title.blue {{ color: #0369A1; }}
        .stage-title.purple {{ color: #7E22CE; }}

        .stage-desc {{
            font-size: 0.9rem;
            color: #64748B;
            margin-bottom: 14px;
            font-weight: 500;
        }}

        .stage-btn {{
            background: transparent;
            border-width: 1.5px;
            border-style: solid;
            border-radius: 30px;
            padding: 6px 18px;
            font-size: 0.88rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }}
        .stage-btn:hover {{ transform: translateX(-4px); }}

        .stage-btn.green {{ border-color: #22C55E; color: #16A34A; }}
        .stage-btn.green:hover {{ background: #22C55E; color: white; }}
        .stage-btn.blue {{ border-color: #3B82F6; color: #2563EB; }}
        .stage-btn.blue:hover {{ background: #3B82F6; color: white; }}
        .stage-btn.purple {{ border-color: #A855F7; color: #9333EA; }}
        .stage-btn.purple:hover {{ background: #A855F7; color: white; }}

        .courses-view {{
            display: none;
            flex-direction: column;
            gap: 20px;
            animation: fadeIn 0.4s ease-in-out;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .courses-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(255, 255, 255, 0.95);
            padding: 16px 24px;
            border-radius: 20px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.02);
        }}

        .stage-tag {{
            background: #5D45FD;
            color: white;
            padding: 6px 20px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 1rem;
        }}

        .back-btn {{
            background: transparent;
            border: 1.5px solid #64748B;
            color: #64748B;
            border-radius: 20px;
            padding: 6px 18px;
            cursor: pointer;
            font-weight: 700;
            font-size: 0.88rem;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }}
        .back-btn:hover {{ background: #64748B; color: white; }}

        .course-details-container {{
            display: flex;
            flex-direction: column;
            gap: 30px;
        }}

        .single-course-block {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 24px;
            padding: 24px;
            border: 1.5px solid #E2E8F0;
            box-shadow: 0 8px 25px rgba(0,0,0,0.03);
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}

        .course-code-header {{
            font-size: 1.4rem;
            font-weight: 800;
            color: #1E1B4B;
            border-bottom: 2px solid #F1F5F9;
            padding-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .chapters-badge {{
            background: #EEF2FF;
            color: #4F46E5;
            font-size: 0.88rem;
            padding: 4px 12px;
            border-radius: 20px;
            font-weight: 700;
            border: 1px solid #C7D2FE;
        }}

        .course-content-layout {{
            display: flex;
            gap: 20px;
            align-items: stretch;
        }}

        .brief-card {{
            background: #F8F7FF;
            border-radius: 18px;
            padding: 20px;
            width: 280px;
            min-width: 280px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            border: 1px solid #EDE9FE;
        }}

        .brief-title {{
            font-size: 1.1rem;
            font-weight: 800;
            color: #1E1B4B;
            margin-bottom: 12px;
            text-align: center;
        }}

        .brief-text {{
            font-size: 0.9rem;
            color: #475569;
            line-height: 1.6;
            text-align: right;
            margin-bottom: 15px;
        }}

        .brief-btn {{
            background: #5D45FD;
            color: white;
            border: none;
            border-radius: 12px;
            padding: 10px;
            font-weight: 700;
            font-size: 0.9rem;
            cursor: pointer;
            width: 100%;
            transition: background 0.2s ease;
        }}
        .brief-btn:hover {{ background: #4B32E4; }}

        .topics-grid {{
            display: grid;
            gap: 15px;
            flex: 1;
        }}

        .topics-grid.cols-2 {{ grid-template-columns: repeat(2, 1fr); }}
        .topics-grid.cols-3 {{ grid-template-columns: repeat(3, 1fr); }}
        .topics-grid.cols-4 {{ grid-template-columns: repeat(4, 1fr); }}

        .topic-card {{
            background: #FFFFFF;
            border: 1.5px solid #E2E8F0;
            border-radius: 18px;
            padding: 20px 14px 14px 14px;
            min-height: 195px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.02);
            transition: all 0.25s ease;
            cursor: pointer;
            position: relative;
        }}
        .topic-card:hover {{
            transform: translateY(-5px);
            border-color: #5D45FD;
            box-shadow: 0 8px 20px rgba(93, 69, 253, 0.12);
        }}

        .topic-icon {{
            height: 56px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 6px;
            direction: ltr !important;
            unicode-bidi: isolate;
        }}

        .topic-title {{
            font-size: 0.98rem;
            font-weight: 800;
            color: #1E1B4B;
            margin-bottom: 10px;
            line-height: 1.35;
        }}

        .topic-progress-bar {{
            width: 90%;
            height: 6px;
            background: #E2E8F0;
            border-radius: 6px;
            margin-bottom: 10px;
            overflow: hidden;
        }}

        .topic-progress-fill {{
            height: 100%;
            background: #5D45FD;
            border-radius: 6px;
            transition: width 0.4s ease, background 0.3s ease;
        }}

        .topic-progress-fill.completed {{
            background: #10B981 !important;
        }}

        .topic-footer {{
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 4px;
        }}

        .topic-count {{
            font-size: 0.85rem;
            color: #475569;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .topic-percent {{
            font-size: 0.8rem;
            font-weight: 800;
            color: #5D45FD;
        }}
        .topic-percent.completed {{
            color: #10B981;
        }}

        .lessons-list {{
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-top: 15px;
            max-height: 380px;
            overflow-y: auto;
        }}

        .lesson-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #F8FAFC;
            border: 1.5px solid #E2E8F0;
            border-radius: 14px;
            padding: 12px 16px;
            transition: all 0.2s ease;
        }}
        .lesson-row:hover {{
            background: #F1F5F9;
            border-color: #CBD5E1;
        }}
        .lesson-row.is-done {{
            background: #F0FDF4;
            border-color: #BBF7D0;
        }}

        .lesson-info {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex: 1;
        }}

        .lesson-check-btn {{
            background: #FFFFFF;
            border: 2px solid #CBD5E1;
            color: transparent;
            width: 26px;
            height: 26px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 0.75rem;
            transition: all 0.2s ease;
        }}
        .lesson-check-btn.checked {{
            background: #10B981;
            border-color: #10B981;
            color: #FFFFFF;
        }}

        .lesson-name {{
            font-weight: 700;
            font-size: 0.95rem;
            color: #1E1B4B;
        }}
        .lesson-row.is-done .lesson-name {{
            color: #065F46;
            text-decoration: line-through;
            opacity: 0.85;
        }}

        .open-lesson-btn {{
            background: #FFFFFF;
            color: #5D45FD;
            text-decoration: none;
            padding: 7px 14px;
            border-radius: 10px;
            font-size: 0.85rem;
            font-weight: 800;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            border: 1.5px solid #C7D2FE;
            box-shadow: 0 2px 5px rgba(93, 69, 253, 0.08);
            transition: all 0.2s;
        }}
        .open-lesson-btn i {{
            color: #5D45FD !important;
        }}
        .open-lesson-btn:hover {{
            background: #5D45FD;
            color: white;
            border-color: #5D45FD;
            box-shadow: 0 4px 12px rgba(93, 69, 253, 0.2);
            transform: translateY(-2px);
        }}
        .open-lesson-btn:hover i {{
            color: white !important;
        }}

        .tools-section {{
            margin-top: 10px;
            padding-top: 20px;
            border-top: 2px dashed #E2E8F0;
        }}

        .tools-section-title {{
            text-align: center;
            font-size: 1.35rem;
            font-weight: 800;
            color: #1E1B4B;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }}

        .tools-section-title i {{ color: #6366F1; }}

        .tools-grid {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 15px;
        }}

        .tool-card {{
            background: #FFFFFF;
            border-radius: 20px;
            padding: 20px 12px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            text-align: center;
            border: 1.5px solid transparent;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);
            transition: all 0.3s ease;
        }}
        .tool-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.06);
        }}

        .tool-card.notes {{ background: #F4FBF7; border-color: #D1FAE5; }}
        .tool-card.quiz {{ background: #FFFBF4; border-color: #FDE68A; }}
        .tool-card.ai {{ background: #F5F8FF; border-color: #DBEAFE; }}
        .tool-card.grades {{ background: #FAF5FF; border-color: #E9D5FF; }}
        .tool-card.schedule {{ background: #FFF5F5; border-color: #FECDD3; }}

        .tool-icon {{
            font-size: 2.2rem;
            margin-bottom: 12px;
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .tool-card.notes .tool-icon {{ color: #10B981; }}
        .tool-card.quiz .tool-icon {{ color: #F59E0B; }}
        .tool-card.ai .tool-icon {{ color: #3B82F6; }}
        .tool-card.grades .tool-icon {{ color: #9333EA; }}
        .tool-card.schedule .tool-icon {{ color: #F43F5E; }}

        .tool-title {{
            font-size: 1.05rem;
            font-weight: 800;
            margin-bottom: 6px;
        }}
        .tool-card.notes .tool-title {{ color: #047857; }}
        .tool-card.quiz .tool-title {{ color: #B45309; }}
        .tool-card.ai .tool-title {{ color: #1D4ED8; }}
        .tool-card.grades .tool-title {{ color: #7E22CE; }}
        .tool-card.schedule .tool-title {{ color: #BE123C; }}

        .tool-desc {{
            font-size: 0.8rem;
            color: #64748B;
            line-height: 1.4;
            margin-bottom: 16px;
            min-height: 38px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .tool-btn {{
            width: 100%;
            padding: 8px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 0.85rem;
            background: #FFFFFF;
            border-width: 1.5px;
            border-style: solid;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .tool-card.notes .tool-btn {{ border-color: #10B981; color: #10B981; }}
        .tool-card.notes .tool-btn:hover {{ background: #10B981; color: white; }}
        .tool-card.quiz .tool-btn {{ border-color: #F59E0B; color: #F59E0B; }}
        .tool-card.quiz .tool-btn:hover {{ background: #F59E0B; color: white; }}
        .tool-card.ai .tool-btn {{ border-color: #3B82F6; color: #3B82F6; }}
        .tool-card.ai .tool-btn:hover {{ background: #3B82F6; color: white; }}
        .tool-card.grades .tool-btn {{ border-color: #A855F7; color: #9333EA; }}
        .tool-card.grades .tool-btn:hover {{ background: #A855F7; color: white; }}
        .tool-card.schedule .tool-btn {{ border-color: #F43F5E; color: #F43F5E; }}
        .tool-card.schedule .tool-btn:hover {{ background: #F43F5E; color: white; }}

        .exam-form-card {{
            background: #FFF5F5;
            border: 1.5px solid #FECDD3;
            border-radius: 18px;
            padding: 20px;
            margin-bottom: 20px;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }}
        .exam-form-group {{
            display: flex;
            flex-direction: column;
            gap: 6px;
            text-align: right;
            position: relative;
        }}
        .exam-form-label {{
            font-size: 0.88rem;
            font-weight: 700;
            color: #881337;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .exam-input, .exam-select {{
            width: 100%;
            padding: 11px 14px;
            border-radius: 12px;
            border: 1.5px solid #E2E8F0;
            font-size: 0.92rem;
            outline: none;
            background: white;
            color: #1E1B4B;
            transition: all 0.2s;
        }}
        .exam-input:focus, .exam-select:focus {{
            border-color: #F43F5E;
            box-shadow: 0 0 0 3px rgba(244, 63, 94, 0.1);
        }}
        .exam-select {{
            appearance: none;
            -webkit-appearance: none;
            -moz-appearance: none;
            background-color: white;
            background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%231E1B4B' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
            background-repeat: no-repeat;
            background-position: left 24px center;
            background-size: 14px;
            padding-left: 45px !important;
            cursor: pointer;
        }}
        .exam-row-two-cols {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }}
        .alarm-time-field {{
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: white;
            padding: 11px 14px;
            border-radius: 12px;
            border: 1.5px solid #E2E8F0;
            color: #1E1B4B;
            font-size: 0.92rem;
            font-weight: 700;
        }}
        .alarm-time-field:hover {{
            border-color: #F43F5E;
        }}
        .alarm-picker-box {{
            position: absolute;
            bottom: calc(100% + 8px);
            left: 0;
            width: 100%;
            background: #FFFFFF;
            border: 2px solid #FECDD3;
            border-radius: 20px;
            box-shadow: 0 12px 35px rgba(244, 63, 94, 0.2);
            padding: 16px;
            z-index: 1050;
            display: none;
            flex-direction: column;
            gap: 12px;
            animation: fadeIn 0.2s ease;
        }}
        .alarm-display-row {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            direction: ltr;
        }}
        .alarm-num-box {{
            font-size: 1.8rem;
            font-weight: 800;
            background: #FFF1F2;
            color: #E11D48;
            padding: 6px 14px;
            border-radius: 12px;
            cursor: pointer;
            border: 2px solid transparent;
            min-width: 60px;
            text-align: center;
        }}
        .alarm-num-box.active {{
            border-color: #E11D48;
            background: #FFE4E6;
        }}
        .alarm-period-toggle {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}
        .alarm-period-btn {{
            padding: 4px 10px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 800;
            border: 1.5px solid #E2E8F0;
            background: white;
            cursor: pointer;
        }}
        .alarm-period-btn.active {{
            background: #E11D48;
            color: white;
            border-color: #E11D48;
        }}
        .alarm-dial-container {{
            position: relative;
            width: 170px;
            height: 170px;
            border-radius: 50%;
            background: #FFF1F2;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .alarm-center-dot {{
            width: 8px;
            height: 8px;
            background: #E11D48;
            border-radius: 50%;
            position: absolute;
            z-index: 3;
        }}
        .alarm-hand {{
            position: absolute;
            bottom: 50%;
            left: calc(50% - 1.5px);
            width: 3px;
            height: 60px;
            background: #E11D48;
            transform-origin: bottom center;
            border-radius: 3px;
            transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 2;
        }}
        .alarm-dial-number {{
            position: absolute;
            width: 28px;
            height: 28px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;
            font-weight: 700;
            color: #475569;
            cursor: pointer;
            z-index: 4;
            transition: all 0.15s;
        }}
        .alarm-dial-number:hover, .alarm-dial-number.selected {{
            background: #E11D48;
            color: white;
            font-weight: 800;
            transform: scale(1.1);
        }}
        .alarm-confirm-btn {{
            background: #E11D48;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 8px;
            font-weight: 700;
            font-size: 0.88rem;
            cursor: pointer;
            transition: background 0.2s;
        }}
        .alarm-confirm-btn:hover {{ background: #BE123C; }}

        .add-exam-btn {{
            background: #F43F5E;
            color: white;
            border: none;
            border-radius: 12px;
            padding: 12px 18px;
            font-weight: 800;
            font-size: 0.95rem;
            cursor: pointer;
            transition: background 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            width: 100%;
            margin-top: 4px;
        }}
        .add-exam-btn:hover {{ background: #E11D48; }}
        .exams-list {{
            display: flex;
            flex-direction: column;
            gap: 12px;
            max-height: 320px;
            overflow-y: auto;
        }}
        .exam-item {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #F8FAFC;
            border: 1.5px solid #E2E8F0;
            border-radius: 14px;
            padding: 14px 18px;
            transition: all 0.2s;
        }}
        .exam-item:hover {{
            background: #F1F5F9;
            border-color: #CBD5E1;
        }}
        .exam-item.soon {{
            border-color: #F87171;
            background: #FEF2F2;
        }}
        .exam-badge {{
            padding: 4px 10px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 800;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}
        .exam-badge.soon {{
            background: #FEE2E2;
            color: #DC2626;
        }}
        .exam-badge.safe {{
            background: #E0F2FE;
            color: #0284C7;
        }}
        .exam-badge.past {{
            background: #F1F5F9;
            color: #64748B;
        }}

        .modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(4px);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 1000;
            animation: fadeIn 0.3s ease;
        }}

        .modal-card {{
            background: white;
            border-radius: 24px;
            padding: 25px;
            width: 90%;
            max-width: 820px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
            border: 1px solid #E2E8F0;
            position: relative;
            max-height: 90vh;
            overflow-y: auto;
        }}

        .modal-header {{
            font-size: 1.35rem;
            font-weight: 800;
            color: #1E1B4B;
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #F1F5F9;
            padding-bottom: 10px;
        }}

        .close-modal-btn {{
            background: #F1F5F9;
            border: none;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            font-size: 1.1rem;
            cursor: pointer;
            color: #64748B;
            transition: all 0.2s ease;
        }}
        .close-modal-btn:hover {{ background: #E2E8F0; color: #0F172A; }}

        .upload-zone {{
            border: 2px dashed #A7F3D0;
            background: #F0FDF4;
            border-radius: 18px;
            padding: 25px;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s ease;
            margin-bottom: 20px;
        }}
        .upload-zone:hover {{
            background: #DCFCE7;
            border-color: #10B981;
        }}
        .upload-zone i {{
            font-size: 2.8rem;
            color: #10B981;
            margin-bottom: 10px;
        }}
        .upload-zone h4 {{
            color: #065F46;
            font-size: 1.1rem;
            margin-bottom: 4px;
        }}
        .upload-zone p {{
            color: #64748B;
            font-size: 0.85rem;
        }}

        .notes-list {{
            display: flex;
            flex-direction: column;
            gap: 12px;
            max-height: 280px;
            overflow-y: auto;
        }}

        .note-item {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            padding: 12px 16px;
            transition: all 0.2s;
        }}
        .note-item:hover {{
            background: #F1F5F9;
            border-color: #CBD5E1;
        }}
        .note-info {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex: 1;
            overflow: hidden;
        }}
        .note-info i {{
            font-size: 1.6rem;
            color: #5D45FD;
            min-width: 30px;
        }}
        .note-name {{
            font-weight: 700;
            color: #1E1B4B;
            font-size: 0.95rem;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 250px;
        }}
        .note-size {{
            font-size: 0.78rem;
            color: #64748B;
        }}
        .note-actions {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .open-note-btn {{
            background: #EEF2FF;
            color: #4F46E5;
            text-decoration: none;
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.85rem;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: background 0.2s;
        }}
        .open-note-btn:hover {{
            background: #E0E7FF;
            color: #4338CA;
        }}
        .delete-note-btn {{
            background: #FEE2E2;
            color: #EF4444;
            border: none;
            padding: 6px 12px;
            border-radius: 8px;
            font-size: 0.85rem;
            cursor: pointer;
            font-weight: 700;
            transition: background 0.2s;
        }}
        .delete-note-btn:hover {{
            background: #FCA5A5;
            color: #991B1B;
        }}

        .ai-chat-container {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        .chat-box {{
            background: #F8FAFC;
            border: 1.5px solid #E2E8F0;
            border-radius: 18px;
            padding: 18px;
            height: 360px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        .chat-msg {{
            padding: 12px 16px;
            border-radius: 14px;
            font-size: 0.95rem;
            max-width: 85%;
            line-height: 1.8;
            unicode-bidi: plaintext;
        }}
        .chat-msg.bot {{
            background: #EFF6FF;
            color: #1E3A8A;
            align-self: flex-start;
            border: 1px solid #DBEAFE;
            text-align: right;
        }}
        .chat-msg.user {{
            background: #5D45FD;
            color: white;
            align-self: flex-end;
            text-align: right;
        }}
        .chat-msg img {{
            max-width: 100%;
            border-radius: 8px;
            margin-top: 6px;
            border: 1px solid #CBD5E1;
        }}

        .katex, .katex-html, .katex-display, .math-box {{
            direction: ltr !important;
            unicode-bidi: isolate !important;
            display: inline-block !important;
        }}
        .katex-display {{
            display: block !important;
            text-align: center !important;
            margin: 10px 0 !important;
            width: 100% !important;
        }}

        .board-popup-container {{
            display: none;
            background: #FFFFFF;
            border: 2px dashed #C7D2FE;
            border-radius: 16px;
            padding: 12px;
            text-align: center;
            animation: fadeIn 0.2s ease;
            margin-bottom: 4px;
        }}
        .board-header-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 8px;
        }}
        .board-title {{
            font-size: 0.9rem;
            font-weight: 800;
            color: #4338CA;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        canvas {{
            background: #FFF;
            border: 1.5px solid #CBD5E1;
            border-radius: 12px;
            cursor: crosshair;
            touch-action: none;
            width: 100%;
            max-width: 100%;
            height: 160px;
        }}
        .board-actions {{
            display: flex;
            gap: 10px;
            margin-top: 8px;
            justify-content: center;
        }}
        .board-action-btn {{
            padding: 7px 16px;
            border-radius: 10px;
            font-size: 0.85rem;
            font-weight: 700;
            cursor: pointer;
            border: none;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}
        .board-action-btn.clear {{ background: #FEE2E2; color: #991B1B; }}
        .board-action-btn.send {{ background: #5D45FD; color: white; }}
        .board-action-btn.send:hover {{ background: #4B32E4; }}

        .pro-math-keyboard {{
            display: none;
            background: #F8F9FE;
            border: 1.5px solid #E2E8F0;
            border-radius: 20px;
            padding: 14px;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.08);
            animation: fadeIn 0.2s ease;
            margin-bottom: 8px;
            flex-direction: column;
            gap: 10px;
            direction: ltr;
        }}
        .kb-top-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 4px;
            gap: 10px;
        }}
        .kb-top-bar-title {{
            font-size: 0.85rem;
            font-weight: 800;
            color: #5D45FD;
            display: flex;
            align-items: center;
            gap: 6px;
            white-space: nowrap;
        }}
        .kb-nav-group {{
            display: flex;
            gap: 4px;
            align-items: center;
            background: #FFFFFF;
            border: 1.5px solid #E2E8F0;
            border-radius: 12px;
            padding: 3px;
        }}
        .kb-nav-btn {{
            background: #FFFFFF;
            border: none;
            font-size: 1rem;
            cursor: pointer;
            color: #475569;
            width: 30px;
            height: 30px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.15s;
        }}
        .kb-nav-btn:hover {{ background: #EEF2FF; color: #5D45FD; }}

        .kb-tab-pill {{
            background: #FFFFFF;
            border: 1.5px solid #E2E8F0;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.82rem;
            font-weight: 700;
            cursor: pointer;
            color: #475569;
            transition: all 0.2s;
            white-space: nowrap;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            justify-content: center;
        }}
        .kb-tab-pill:hover {{
            background: #EEF2FF;
            color: #5D45FD;
            border-color: #C7D2FE;
        }}
        .kb-tab-pill.active-tool {{
            background: #5D45FD !important;
            color: white !important;
            border-color: #5D45FD !important;
        }}
        .kb-tab-pill.active-tool i {{ color: white !important; }}

        .kb-category-row {{
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 5px;
        }}
        .kb-category-pill {{
            background: #FFFFFF;
            border: 1.5px solid #E2E8F0;
            border-radius: 12px;
            padding: 8px 4px;
            font-size: 0.74rem;
            font-weight: 800;
            color: #64748B;
            cursor: pointer;
            text-align: center;
            transition: all 0.18s;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        .kb-category-pill:hover {{
            border-color: #C7D2FE;
            background: #EEF2FF;
            color: #5D45FD;
        }}
        .kb-category-pill.active-pill {{
            background: #5D45FD !important;
            color: #FFFFFF !important;
            border-color: #5D45FD !important;
            box-shadow: 0 4px 10px rgba(93, 69, 253, 0.25);
        }}

        .kb-grid-layout {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 7px;
        }}
        .kb-grid-key {{
            background: #FFFFFF !important;
            border: 1.5px solid #E2E8F0;
            border-radius: 12px;
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.05rem;
            font-weight: 700;
            color: #1E1B4B !important;
            cursor: pointer;
            transition: all 0.12s;
            font-family: 'KaTeX_Math', 'Times New Roman', serif;
            line-height: 1;
            padding: 2px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.02);
        }}
        .kb-grid-key:active {{
            transform: scale(0.94);
        }}
        .kb-grid-key.number {{
            font-weight: 800;
            font-size: 1.2rem;
        }}
        .kb-grid-key.func-key {{
            font-size: 0.86rem;
            font-weight: 700;
        }}
        .kb-grid-key:hover {{
            border-color: #5D45FD !important;
            background: #EEF2FF !important;
            color: #5D45FD !important;
            box-shadow: 0 3px 10px rgba(93, 69, 253, 0.12);
        }}

        .kb-sup {{ font-size: 0.62em; vertical-align: super; margin-right: 1px; }}
        .kb-sub {{ font-size: 0.62em; vertical-align: sub; margin-right: 1px; }}

        .chat-icon-btn.recording {{
            background: #EF4444 !important;
            color: white !important;
            animation: pulseRecord 1.2s infinite;
        }}
        @keyframes pulseRecord {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.12); }}
            100% {{ transform: scale(1); }}
        }}

        .chat-input-row {{
            display: flex;
            gap: 8px;
            align-items: center;
            background: #FFFFFF;
            padding: 8px 12px;
            border-radius: 16px;
            border: 1.5px solid #E2E8F0;
        }}
        .chat-icon-btn {{
            background: #EEF2FF;
            color: #4F46E5;
            border: none;
            width: 38px;
            height: 38px;
            border-radius: 10px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.1rem;
            transition: all 0.2s;
        }}
        .chat-icon-btn:hover, .chat-icon-btn.active {{
            background: #5D45FD;
            color: white;
        }}
        .chat-text-input {{
            flex: 1;
            border: none;
            outline: none;
            padding: 8px 10px;
            font-size: 0.95rem;
            background: transparent;
            color: #1E1B4B;
        }}
        .chat-send-btn {{
            background: #5D45FD;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 10px;
            font-weight: 700;
            font-size: 0.9rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: background 0.2s;
        }}
        .chat-send-btn:hover {{ background: #4B32E4; }}

        .quiz-config-card {{
            background: #FFFDF5;
            border: 1.5px solid #FDE68A;
            border-radius: 18px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}
        .quiz-option-row {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .quiz-radio-label {{
            flex: 1;
            min-width: 140px;
            padding: 10px 14px;
            background: white;
            border: 1.5px solid #E2E8F0;
            border-radius: 12px;
            cursor: pointer;
            text-align: center;
            font-weight: 700;
            font-size: 0.88rem;
            color: #1E1B4B;
            transition: all 0.2s;
        }}
        .quiz-radio-label:hover, .quiz-radio-label.active {{
            border-color: #F59E0B;
            background: #FEF3C7;
            color: #B45309;
        }}
        .quiz-question-box {{
            background: #F8FAFC;
            border: 1.5px solid #E2E8F0;
            border-radius: 16px;
            padding: 20px;
            margin-bottom: 18px;
        }}
        .quiz-mcq-opt {{
            display: flex;
            align-items: center;
            justify-content: flex-start;
            gap: 14px;
            background: white;
            border: 1.5px solid #E2E8F0;
            border-radius: 12px;
            padding: 12px 16px;
            margin-top: 8px;
            cursor: pointer;
            transition: all 0.2s;
            direction: rtl;
        }}
        .quiz-mcq-opt:hover, .quiz-mcq-opt.selected {{
            border-color: #5D45FD;
            background: #EEF2FF;
        }}

        .footer {{
            text-align: center;
            padding: 20px 25px;
            background: rgba(255, 255, 255, 0.88);
            backdrop-filter: blur(5px);
            border-radius: 20px;
            border: 1px solid rgba(226, 232, 240, 0.6);
            margin-top: 10px;
        }}
        .footer-title {{ font-size: 1.2rem; font-weight: 800; color: #1E1B4B; margin-bottom: 4px; }}
        .footer-desc {{ font-size: 0.95rem; color: #64748B; }}
        .footer-highlight {{ margin-top: 6px; font-size: 1.1rem; font-weight: 800; color: #5D45FD; }}

        @media (max-width: 1024px) {{
            .stages-grid {{ grid-template-columns: 1fr; }}
            .course-content-layout {{ flex-direction: column-reverse; }}
            .brief-card {{ width: 100%; min-width: 100%; }}
            .topics-grid.cols-2, .topics-grid.cols-3, .topics-grid.cols-4 {{ grid-template-columns: repeat(2, 1fr); }}
            .tools-grid {{ grid-template-columns: repeat(3, 1fr); }}
            .exam-row-two-cols {{ grid-template-columns: 1fr; }}
            .kb-category-row {{ grid-template-columns: repeat(3, 1fr); }}
        }}
        @media (max-width: 640px) {{
            .topics-grid.cols-2, .topics-grid.cols-3, .topics-grid.cols-4 {{ grid-template-columns: 1fr; }}
            .tools-grid {{ grid-template-columns: repeat(2, 1fr); }}
            .kb-category-row {{ grid-template-columns: repeat(3, 1fr); }}
        }}
    </style>
</head>
<body>
    <div class="main-container">
        <div class="header-section">
            <h1 class="main-title">Math<span>Rise</span></h1>
            <p class="main-subtitle">مرحباً بك في منصتك الذكية لتعلم الرياضيات وفهمها بعمق</p>
            <div class="divider"></div>
        </div>

        <div id="stagesView">
            <p class="choose-text" style="text-align: center; margin-bottom: 20px;">اختر مرحلتك الدراسية للبدء</p>
            <div class="stages-grid">
                <div class="stage-card green">
                    <div class="icon-circle green"><i class="fas fa-book-open book-icon"></i></div>
                    <div class="card-content">
                        <div class="stage-title green">أول ثانوي</div>
                        <div class="stage-desc">بداية رحلتك نحو التفوق</div>
                        <button class="stage-btn green" onclick="showCourses('أول ثانوي')">استكشف المقررات <i class="fas fa-chevron-left"></i></button>
                    </div>
                </div>

                <div class="stage-card blue">
                    <div class="icon-circle blue"><i class="fas fa-book-open book-icon"></i></div>
                    <div class="card-content">
                        <div class="stage-title blue">ثاني ثانوي</div>
                        <div class="stage-desc">طور مهاراتك وثق بقدراتك</div>
                        <button class="stage-btn blue" onclick="showCourses('ثاني ثانوي')">استكشف المقررات <i class="fas fa-chevron-left"></i></button>
                    </div>
                </div>

                <div class="stage-card purple">
                    <div class="icon-circle purple"><i class="fas fa-book-open book-icon"></i></div>
                    <div class="card-content">
                        <div class="stage-title purple">ثالث ثانوي</div>
                        <div class="stage-desc">استعد للمستقبل بكل ثقة</div>
                        <button class="stage-btn purple" onclick="showCourses('ثالث ثانوي')">استكشف المقررات <i class="fas fa-chevron-left"></i></button>
                    </div>
                </div>
            </div>
        </div>

        <div id="coursesView" class="courses-view">
            <div class="courses-header">
                <span class="stage-tag" id="currentStageTitle">ثالث ثانوي</span>
                <span style="font-weight: 800; color: #1E1B4B; font-size: 1.1rem;"><i class="fas fa-book-bookmark" style="color: #5D45FD;"></i> مقررات ومواضيع المرحلة</span>
                <button class="back-btn" onclick="showStages()"><i class="fas fa-arrow-right"></i> العودة للمراحل</button>
            </div>
            <div class="course-details-container" id="coursesContent"></div>
        </div>

        <div class="footer">
            <div class="footer-title">🎯 هدفنا</div>
            <div class="footer-desc">تمكينك من فهم الرياضيات بعمق، وتطوير مهاراتك، وتحقيق أفضل النتائج.</div>
            <div class="footer-highlight">🚀 رحلتك نحو التفوق تبدأ من هنا!</div>
        </div>
    </div>

    <div class="modal-overlay" id="detailsModal">
        <div class="modal-card">
            <div class="modal-header">
                <span id="modalCourseTitle">نافذة المقرر</span>
                <button class="close-modal-btn" onclick="closeModal()"><i class="fas fa-times"></i></button>
            </div>
            <div id="modalCourseBody"></div>
        </div>
    </div>

    <script>
        const GEMINI_API_KEY = "{gemini_api_key}";
        const QUESTIONS_BANK = {questions_bank_json_str};
        const MATH366_BOOK_CONTEXT = {math366_context_json_str};

        let currentActiveStage = 'ثالث ثانوي';
        let currentActiveCourse = 'ريض 366';
        let chatMessagesHistory = [];
        let uploadedNotesStore = {{}};

        let recognition = null;
        let isRecording = false;
        let isSavingManualGrade = false;

        let currentQuizState = {{
            courseCode: '',
            scope: 'all',
            selectedTopics: [],
            qType: 'mix',
            numQuestions: 3,
            questions: [],
            studentAnswers: {{}},
            evaluationResults: null
        }};

        let activeEssayInputId = null;

        const BOOK_URLS = {{
            "ريض 151": "https://www.edunet.bh/e_content/level_3/stage_10/subject_ID_28/Part_3/e_books/Math151SB/Math151SB/index.html",
            "ريض 152": "https://www.edunet.bh/e_content/level_3/stage_10/subject_ID_28/Part_3/e_books/Maths-152-2024(1)/Maths%20152%202024/index.html",
            "ريض 261": "https://www.edunet.bh/e_content/level_3/stage_10/subject_ID_28/Part_3/e_books/MATH253-261/MATH253-261/index.html",
            "ريض 364": "https://www.edunet.bh/e_content/level_3/stage_10/subject_ID_28/Part_3/e_books/Math363SB/Math363SB/index.html",
            "ريض 366": "https://www.edunet.bh/e_content/level_3/stage_10/subject_ID_28/Part_3/e_books/Maths-366-2015/Maths%20366%202015/index.html"
        }};

        let pickerState = {{
            hour: '08',
            minute: '30',
            period: 'AM',
            mode: 'hours'
        }};

        const courseIcons = {{
            matrix_1x1: `
                <svg width="50" height="50" viewBox="0 0 50 50">
                    <path d="M 15,9 L 8,9 L 8,41 L 15,41" fill="none" stroke="#5D45FD" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
                    <text x="25" y="32" font-family="'Times New Roman', Times, serif" font-style="italic" font-weight="bold" font-size="24" fill="#5D45FD" text-anchor="middle">a</text>
                    <path d="M 35,9 L 42,9 L 42,41 L 35,41" fill="none" stroke="#5D45FD" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>`,

            inequality_number_line: `
                <svg width="50" height="50" viewBox="0 0 50 50">
                    <line x1="4" y1="25" x2="46" y2="25" stroke="#5D45FD" stroke-width="3" stroke-linecap="round"/>
                    <polyline points="10,19 4,25 10,31" fill="none" stroke="#5D45FD" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                    <polyline points="40,19 46,25 40,31" fill="none" stroke="#5D45FD" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                    <line x1="16" y1="25" x2="34" y2="25" stroke="#5D45FD" stroke-width="6" stroke-linecap="round"/>
                    <circle cx="16" cy="25" r="5.5" fill="#5D45FD"/>
                    <circle cx="34" cy="25" r="5" fill="white" stroke="#5D45FD" stroke-width="3"/>
                </svg>`,
            linear_coord_system: `
                <svg width="50" height="50" viewBox="0 0 50 50">
                    <line x1="5" y1="25" x2="45" y2="25" stroke="#CBD5E1" stroke-width="2.2"/>
                    <line x1="25" y1="5" x2="25" y2="45" stroke="#CBD5E1" stroke-width="2.2"/>
                    <line x1="8" y1="42" x2="42" y2="8" stroke="#5D45FD" stroke-width="3.2" stroke-linecap="round"/>
                    <circle cx="25" cy="25" r="3" fill="#1E1B4B"/>
                </svg>`,
            parabola_curve: `
                <svg width="50" height="50" viewBox="0 0 50 50">
                    <line x1="5" y1="30" x2="45" y2="30" stroke="#CBD5E1" stroke-width="2.2"/>
                    <line x1="25" y1="5" x2="25" y2="45" stroke="#CBD5E1" stroke-width="2.2"/>
                    <path d="M 10,12 Q 25,48 40,12" fill="none" stroke="#5D45FD" stroke-width="3.2" stroke-linecap="round"/>
                    <circle cx="25" cy="30" r="3.5" fill="#5D45FD"/>
                </svg>`,

            right_triangle_shape: `
                <svg width="48" height="48" viewBox="0 0 48 48">
                    <polygon points="7,41 41,41 7,7" fill="none" stroke="#5D45FD" stroke-width="3.2" stroke-linejoin="round"/>
                    <rect x="7" y="31" width="10" height="10" fill="none" stroke="#5D45FD" stroke-width="2.4"/>
                </svg>`,
            circle_shape: `
                <svg width="48" height="48" viewBox="0 0 48 48">
                    <circle cx="24" cy="24" r="18" fill="none" stroke="#5D45FD" stroke-width="3.2"/>
                    <circle cx="24" cy="24" r="2.5" fill="#5D45FD"/>
                    <line x1="24" y1="24" x2="39.5" y2="14.5" stroke="#5D45FD" stroke-width="2.2" stroke-dasharray="2.5,2.5"/>
                </svg>`,

            derivative_svg: `
                <svg width="52" height="52" viewBox="0 0 52 52">
                    <text x="26" y="20" font-family="'Times New Roman', Times, serif" font-style="italic" font-weight="bold" font-size="20" fill="#5D45FD" text-anchor="middle">dy</text>
                    <line x1="10" y1="26" x2="42" y2="26" stroke="#5D45FD" stroke-width="3" stroke-linecap="round"/>
                    <text x="26" y="46" font-family="'Times New Roman', Times, serif" font-style="italic" font-weight="bold" font-size="20" fill="#5D45FD" text-anchor="middle">dx</text>
                </svg>`,
            tangent_max_svg: `
                <svg width="50" height="50" viewBox="0 0 50 50">
                    <line x1="5" y1="44" x2="45" y2="44" stroke="#CBD5E1" stroke-width="2"/>
                    <line x1="6" y1="5" x2="6" y2="45" stroke="#CBD5E1" stroke-width="2"/>
                    <path d="M 8,38 C 18,36 20,12 30,12 C 40,12 42,34 46,34" fill="none" stroke="#5D45FD" stroke-width="3.2" stroke-linecap="round"/>
                    <line x1="18" y1="12" x2="42" y2="12" stroke="#F43F5E" stroke-width="2.5" stroke-dasharray="3,3"/>
                    <circle cx="30" cy="12" r="3.5" fill="#F43F5E"/>
                </svg>`,
            integral_indefinite_svg: `
                <svg width="50" height="50" viewBox="0 0 50 50">
                    <text x="16" y="40" font-family="'Times New Roman', Times, serif" font-size="44" fill="#5D45FD" text-anchor="middle">∫</text>
                    <text x="34" y="32" font-family="'Times New Roman', Times, serif" font-style="italic" font-weight="bold" font-size="22" fill="#5D45FD" text-anchor="middle">dx</text>
                </svg>`,
            integral_definite_svg: `
                <svg width="52" height="52" viewBox="0 0 52 52">
                    <text x="16" y="41" font-family="'Times New Roman', Times, serif" font-size="44" fill="#5D45FD" text-anchor="middle">∫</text>
                    <text x="26" y="16" font-family="'Times New Roman', Times, serif" font-style="italic" font-weight="bold" font-size="13" fill="#5D45FD" text-anchor="middle">b</text>
                    <text x="23" y="51" font-family="'Times New Roman', Times, serif" font-style="italic" font-weight="bold" font-size="13" fill="#5D45FD" text-anchor="middle">a</text>
                    <text x="40" y="32" font-family="'Times New Roman', Times, serif" font-style="italic" font-weight="bold" font-size="20" fill="#5D45FD" text-anchor="middle">dx</text>
                </svg>`,

            trig_identity: `
                <div class="math-badge-icon" style="flex-direction: column; gap: 2px;">
                    <span style="font-size: 1.05rem; letter-spacing: 0.5px; color: #5D45FD; font-weight: 800;">sin²θ + cos²θ = 1</span>
                </div>`,
            func_analysis: `
                <div class="math-badge-icon" style="flex-direction: column; gap: 2px;">
                    <span style="font-size: 1.3rem; color: #5D45FD; font-weight: 800;">f(x) → y</span>
                </div>`,
            limits_diff: `
                <div class="math-badge-icon" style="flex-direction: column; gap: 2px;">
                    <span style="font-size: 1.2rem; color: #5D45FD; font-weight: 800;">lim f(x)</span>
                </div>`,

            probability: `
                <div class="math-badge-icon" style="flex-direction: column; gap: 2px;">
                    <span style="font-size: 1.25rem; color: #5D45FD; font-weight: 800;">P(A ∩ B)</span>
                </div>`,
            rational_func: `
                <div class="math-badge-icon" style="flex-direction: column; gap: 2px;">
                    <span style="font-size: 1.25rem; color: #5D45FD; font-weight: 800;">f(x) = 1/x</span>
                </div>`,

            algebra_chapter: `
                <svg width="48" height="48" viewBox="0 0 48 48">
                    <circle cx="24" cy="24" r="20" fill="none" stroke="#5D45FD" stroke-width="3" stroke-dasharray="6,4"/>
                    <text x="24" y="31" font-family="'Times New Roman', Times, serif" font-weight="bold" font-size="22" fill="#5D45FD" text-anchor="middle">x</text>
                </svg>`,
            geometry_chapter: `
                <svg width="48" height="48" viewBox="0 0 48 48">
                    <polygon points="24,6 42,40 6,40" fill="none" stroke="#5D45FD" stroke-width="3.2" stroke-linejoin="round"/>
                    <circle cx="24" cy="28" r="3" fill="#5D45FD"/>
                </svg>`
        }};

        const coursesData = {{
            "ثالث ثانوي": [
                {{
                    code: "ريض 364",
                    chaptersCount: 3,
                    brief: "",
                    details: "يتناول هذا المقرر دراسة متعمقة للمتطابقات والمعادلات المثلثية، تحليل خصائص الدوال والاتصال، مع دراسة النهايات والاشتقاق وتطبيقات المساحة والتكامل.",
                    topics: [
                        {{ 
                            id: "m364_t1", 
                            title: "المتطابقات والمعادلات المثلثية", 
                            iconHtml: courseIcons.trig_identity,
                            lessons: [
                                {{ id: "m364_t1_l1", title: "1-1 المتطابقات المثلثية", page: 10 }},
                                {{ id: "m364_t1_l2", title: "1-2 إثبات صحة المتطابقات المثلثية", page: 17 }},
                                {{ id: "m364_t1_l3", title: "1-3 المتطابقات المثلثية لمجموع زاويتين والفرق بينهما", page: 22 }},
                                {{ id: "m364_t1_l4", title: "1-4 المتطابقات المثلثية لضعف الزاوية ونصفها", page: 29 }},
                                {{ id: "m364_t1_l5", title: "1-5 حل المعادلات المثلثية", page: 37 }}
                            ]
                        }},
                        {{ 
                            id: "m364_t2", 
                            title: "تحليل الدوال", 
                            iconHtml: courseIcons.func_analysis,
                            lessons: [
                                {{ id: "m364_t2_l1", title: "2-1 الدوال", page: 50 }},
                                {{ id: "m364_t2_l2", title: "2-2 تحليل التمثيلات البيانية للدوال والعلاقات", page: 58 }},
                                {{ id: "m364_t2_l3", title: "2-3 الاتصال وسلوك طرفي التمثيل البياني والنهايات", page: 68 }},
                                {{ id: "m364_t2_l4", title: "2-4 القيم القصوى ومتوسط معدل التغير", page: 79 }},
                                {{ id: "m364_t2_l5", title: "2-5 الدوال الأم والتحويلات الهندسية", page: 89 }},
                                {{ id: "m364_t2_l6", title: "2-6 العمليات على الدوال وتركيب دالتين", page: 98 }},
                                {{ id: "m364_t2_l7", title: "2-7 العلاقات والدوال العكسية", page: 105 }}
                            ]
                        }},
                        {{ 
                            id: "m364_t3", 
                            title: "النهايات والاشتقاق", 
                            iconHtml: courseIcons.limits_diff,
                            lessons: [
                                {{ id: "m364_t3_l1", title: "3-1 تقدير النهايات بيانياً", page: 122 }},
                                {{ id: "m364_t3_l2", title: "3-2 حساب النهايات جبرياً", page: 131 }},
                                {{ id: "m364_t3_l3", title: "3-3 المماس والسرعة المتجهة", page: 142 }}
                            ]
                        }}
                    ]
                }},
                {{
                    code: "ريض 366",
                    chaptersCount: 4,
                    brief: "",
                    details: "يشتمل هذا المقرر على دراسة متعمقة للاشتقاق وتطبيقاته في إيجاد القيم العظمى والصغرى ورسم المنحنيات، بالإضافة إلى حساب التكامل غير المحدد والمحدد وتطبيقات المساحات والحجوم.",
                    topics: [
                        {{ 
                            id: "m366_ch1", 
                            title: "الاشتقاق", 
                            iconHtml: courseIcons.derivative_svg,
                            lessons: [
                                {{ id: "m366_l1", title: "مشتقة تركيب دالتين", page: 12 }},
                                {{ id: "m366_l2", title: "مشتقات الدوال المثلثية", page: 24 }},
                                {{ id: "m366_l3", title: "المشتقات العليا", page: 36 }}
                            ]
                        }},
                        {{ 
                            id: "m366_ch2", 
                            title: "تطبيقات المشتقة", 
                            iconHtml: courseIcons.tangent_max_svg,
                            lessons: [
                                {{ id: "m366_l4", title: "تطبيقات هندسية", page: 44 }},
                                {{ id: "m366_l5", title: "تطبيقات فيزيائية", page: 56 }},
                                {{ id: "m366_l6", title: "المعدلات الزمنية المرتبطة", page: 64 }},
                                {{ id: "m366_l7", title: "تطبيقات المشتقة الأولى والثانية", page: 71 }},
                                {{ id: "m366_l8", title: "التمثيل البياني لمنحنيات دوال كثيرات الحدود", page: 84 }},
                                {{ id: "m366_l9", title: "تطبيقات على القيم العظمى والصغرى", page: 89 }}
                            ]
                        }},
                        {{ 
                            id: "m366_ch3", 
                            title: "التكامل غير المحدد", 
                            iconHtml: courseIcons.integral_indefinite_svg,
                            lessons: [
                                {{ id: "m366_l10", title: "العلاقة بين التفاضل والتكامل", page: 100 }},
                                {{ id: "m366_l11", title: "التكامل غير المحدد", page: 103 }},
                                {{ id: "m366_l12", title: "تطبيقات على التكامل غير المحدد", page: 112 }}
                            ]
                        }},
                        {{ 
                            id: "m366_ch4", 
                            title: "التكامل المحدد", 
                            iconHtml: courseIcons.integral_definite_svg,
                            lessons: [
                                {{ id: "m366_l13", title: "النظرية الأساسية للتفاضل والتكامل", page: 124 }},
                                {{ id: "m366_l14", title: "تطبيقات هندسية على التكامل المحدد", page: 131 }},
                                {{ id: "m366_l15", title: "التكامل بالتعويض", page: 141 }}
                            ]
                        }}
                    ]
                }}
            ],
            "ثاني ثانوي": [
                {{
                    code: "ريض 261",
                    chaptersCount: 2,
                    brief: "",
                    details: "يركز هذا المقرر على تمثيل فضاء العينة والاحتمال بالتباديل والتوافيق، وحساب احتمالات الأحداث المستقلة والمتنافية، بالإضافة إلى تبسيط الدوال والتعابير النسبية وحل معادلاتها.",
                    topics: [
                        {{ 
                            id: "m261_t1", 
                            title: "الاحتمال والقياس", 
                            iconHtml: courseIcons.probability,
                            lessons: [
                                {{ id: "m261_l1", title: "3-1 تمثيل فضاء العينة", page: 114 }},
                                {{ id: "m261_l2", title: "3-2 الاحتمال باستعمال التباديل والتوافيق", page: 120 }},
                                {{ id: "m261_l3", title: "3-3 الاحتمال الهندسي", page: 128 }},
                                {{ id: "m261_l4", title: "3-4 احتمالات الأحداث المستقلة والأحداث غير المستقلة", page: 135 }},
                                {{ id: "m261_l5", title: "3-5 احتمالات الأحداث المتنافية", page: 142 }}
                            ]
                        }},
                        {{ 
                            id: "m261_t2", 
                            title: "العلاقات والدوال النسبية", 
                            iconHtml: courseIcons.rational_func,
                            lessons: [
                                {{ id: "m261_l6", title: "4-1 ضرب التعابير النسبية وقسمتها", page: 158 }},
                                {{ id: "m261_l7", title: "4-2 جمع التعابير النسبية وطرحها", page: 167 }},
                                {{ id: "m261_l8", title: "4-3 دوال المقلوب", page: 173 }},
                                {{ id: "m261_l9", title: "4-4 تمثيل الدوال النسبية بيانياً", page: 180 }},
                                {{ id: "m261_l10", title: "4-5 التغيّر", page: 188 }},
                                {{ id: "m261_l11", title: "4-6 حل المعادلات النسبية", page: 195 }}
                            ]
                        }}
                    ]
                }},
                {{
                    code: "ريض 253",
                    chaptersCount: 2,
                    brief: "مقرر ريض 253 يركز على تطوير فهم الطالب لمفاهيم المتجهات والهندسة التحليلية في الفضاء، واستخدامها في دراسة العلاقات الهندسية وحل المشكلات الرياضية. كما يتناول المتتاليات والمتسلسلات العددية، واختبارات تقاربها، ومتسلسلات القوى، مما يساعد الطالب على تطوير مهارات التحليل الرياضي والتفكير المنطقي وحل المسائل الأكثر تقدمًا.",
                    details: "مقرر ريض 253 يركز على تطوير فهم الطالب لمفاهيم المتجهات والهندسة التحليلية في الفضاء، واستخدامها في دراسة العلاقات الهندسية وحل المشكلات الرياضية. كما يتناول المتتاليات والمتسلسلات العددية، واختبارات تقاربها، ومتسلسلات القوى، مما يساعد الطالب على تطوير مهارات التحليل الرياضي والتفكير المنطقي وحل المسائل الأكثر تقدمًا.",
                    topics: [
                        {{ id: "m253_t1", title: "العلاقات والدوال العكسية والجذرية", iconHtml: courseIcons.algebra_chapter, lessons: [{{ id: "m253_l1", title: "العمليات على الدوال", page: 10 }}, {{ id: "m253_l2", title: "العلاقات والدوال العكسية", page: 18 }}] }},
                        {{ id: "m253_t2", title: "الدوال الأسية واللوغاريتمية", iconHtml: courseIcons.func_analysis, lessons: [{{ id: "m253_l3", title: "الدوال الأسية", page: 50 }}, {{ id: "m253_l4", title: "اللوغاريتمات والدوال اللوغاريتمية", page: 60 }}] }}
                    ]
                }},
                {{
                    code: "ريض 262",
                    chaptersCount: 2,
                    brief: "دراسة المتتابعات والمتسلسلات الحسابية والهندسية والدوال المثلثية.",
                    details: "دراسة المتتابعات والمتسلسلات الحسابية والهندسية وإيجاد مجموعها، بالإضافة إلى قوانين الاحتمال الشرطي.",
                    topics: [
                        {{ id: "m262_t1", title: "المتتابعات والمتسلسلات", iconHtml: courseIcons.geometry_chapter, lessons: [{{ id: "m262_l1", title: "المتتابعات بوصفها دوال", page: 10 }}, {{ id: "m262_l2", title: "المتتابعات والمتسلسلات الحسابية", page: 18 }}] }},
                        {{ id: "m262_t2", title: "الدوال المثلثية", iconHtml: courseIcons.trig_identity, lessons: [{{ id: "m262_l3", title: "الدوال المثلثية في المثلثات القائمة", page: 45 }}, {{ id: "m262_l4", title: "الزوايا وقياساتها", page: 55 }}] }}
                    ]
                }}
            ],
            "أول ثانوي": [
                {{
                    code: "ريض 151",
                    chaptersCount: 3,
                    brief: "",
                    details: "مقرر ريض 151 يركز على بناء أساس قوي في الجبر والدوال والمعادلات والمتباينات والتمثيل البياني، ويهيئ الطالب لدراسة المقررات الرياضية الأكثر تقدمًا. كما يتناول أنواعًا مختلفة من الدوال وخصائصها، والعلاقات، والدوال التربيعية، وأنظمة المتباينات والبرمجة الخطية، مما يساعد على تطوير مهارات التحليل وحل المشكلات الرياضية.",
                    topics: [
                        {{ 
                            id: "m151_t1", 
                            title: "المعادلات والمتباينات", 
                            iconHtml: courseIcons.inequality_number_line,
                            lessons: [
                                {{ id: "m151_t1_l1", title: "1-1 المجموعات والفترات", page: 12 }},
                                {{ id: "m151_t1_l2", title: "1-2 حل معادلات القيمة المطلقة", page: 20 }},
                                {{ id: "m151_t1_l3", title: "1-3 حل المتباينات الخطية في متغير واحد", page: 27 }},
                                {{ id: "m151_t1_l4", title: "1-4 حل المتباينات المركبة ومتباينات القيمة المطلقة", page: 34 }}
                            ]
                        }},
                        {{ 
                            id: "m151_t2", 
                            title: "الدوال والمتباينات", 
                            iconHtml: courseIcons.linear_coord_system,
                            lessons: [
                                {{ id: "m151_t2_l1", title: "2-1 المعادلات الخطية بصيغة ميل - مقطع", page: 54 }},
                                {{ id: "m151_t2_l2", title: "2-2 المعادلات الخطية بصيغة نقطة - ميل", page: 64 }},
                                {{ id: "m151_t2_l3", title: "2-3 العلاقات والدوال", page: 73 }},
                                {{ id: "m151_t2_l4", title: "2-4 دوال خاصة", page: 82 }},
                                {{ id: "m151_t2_l5", title: "2-5 دوال القيمة المطلقة", page: 88 }},
                                {{ id: "m151_t2_l6", title: "2-6 تمثيل المتباينات الخطية ومتباينات القيمة المطلقة بيانياً", page: 96 }},
                                {{ id: "m151_t2_l7", title: "2-7 حل أنظمة المتباينات الخطية بيانياً", page: 102 }},
                                {{ id: "m151_t2_l8", title: "2-8 البرمجة الخطية", page: 109 }}
                            ]
                        }},
                        {{ 
                            id: "m151_t3", 
                            title: "الدوال التربيعية", 
                            iconHtml: courseIcons.parabola_curve,
                            lessons: [
                                {{ id: "m151_t3_l1", title: "3-1 تمثيل الدوال التربيعية بيانياً", page: 128 }},
                                {{ id: "m151_t3_l2", title: "3-2 التحويلات الهندسية في التمثيلات البيانية للدوال التربيعية", page: 142 }},
                                {{ id: "m151_t3_l3", title: "3-3 حل المعادلات التربيعية بيانياً", page: 150 }},
                                {{ id: "m151_t3_l4", title: "3-4 الأعداد المركبة", page: 159 }},
                                {{ id: "m151_t3_l5", title: "3-5 حل المعادلات التربيعية جبرياً", page: 165 }}
                            ]
                        }}
                    ]
                }},
                {{
                    code: "ريض 152",
                    chaptersCount: 3,
                    brief: "",
                    details: "مقرر ريض 152 يركز على تطوير مهارات الطالب في استخدام المصفوفات والعمليات المرتبطة بها لحل المشكلات وتنظيم البيانات، إلى جانب توظيف المفاهيم الهندسية والعلاقات الرياضية في تحليل الأشكال وحل المسائل. كما يتناول تطبيقات متنوعة تشمل المثلثات وقوانين الجيب وجيب التمام، والمساحات، والدوائر ومعادلاتها، مما يساعد الطالب على ربط المفاهيم الرياضية بتطبيقاتها العملية وتطوير مهاراته في التحليل وحل المشكلات.",
                    topics: [
                        {{ 
                            id: "m152_t1", 
                            title: "المصفوفات", 
                            iconHtml: courseIcons.matrix_1x1,
                            lessons: [
                                {{ id: "m152_t1_l1", title: "1-1 مقدمة في المصفوفات", page: 12 }},
                                {{ id: "m152_t1_l2", title: "1-2 العمليات على المصفوفات", page: 19 }},
                                {{ id: "m152_t1_l3", title: "1-3 ضرب المصفوفات", page: 28 }},
                                {{ id: "m152_t1_l4", title: "1-4 المحددات وقاعدة كرامر", page: 35 }}
                            ]
                        }},
                        {{ 
                            id: "m152_t2", 
                            title: "المثلثات القائمة وحساب المثلثات", 
                            iconHtml: courseIcons.right_triangle_shape,
                            lessons: [
                                {{ id: "m152_t2_l1", title: "2-1 المسافة ونقطة المنتصف", page: 54 }},
                                {{ id: "m152_t2_l2", title: "2-2 الوسط الهندسي", page: 67 }},
                                {{ id: "m152_t2_l3", title: "2-3 حساب المثلثات", page: 79 }},
                                {{ id: "m152_t2_l4", title: "2-4 زوايا الارتفاع وزوايا الانخفاض", page: 90 }},
                                {{ id: "m152_t2_l5", title: "2-5 قانون الجيب وقانون جيب التمام", page: 98 }}
                            ]
                        }},
                        {{ 
                            id: "m152_t3", 
                            title: "الدائرة", 
                            iconHtml: courseIcons.circle_shape,
                            lessons: [
                                {{ id: "m152_t3_l1", title: "3-1 الدائرة ومحيطها", page: 120 }},
                                {{ id: "m152_t3_l2", title: "3-2 قياس الزوايا والأقواس", page: 129 }},
                                {{ id: "m152_t3_l3", title: "3-3 الأقواس والأوتار", page: 138 }},
                                {{ id: "m152_t3_l4", title: "3-4 الزوايا المحيطية", page: 147 }},
                                {{ id: "m152_t3_l5", title: "3-5 المماسات", page: 155 }},
                                {{ id: "m152_t3_l6", title: "3-6 معادلة الدائرة", page: 164 }}
                            ]
                        }}
                    ]
                }}
            ]
        }};

        function calculateTopicProgress(lessons) {{
            if (!lessons || lessons.length === 0) return {{ percent: 0, completedCount: 0, totalCount: 0 }};
            let done = 0;
            lessons.forEach(l => {{
                if (localStorage.getItem('mathrise_lesson_' + l.id) === 'true') {{
                    done++;
                }}
            }});
            const percent = Math.round((done / lessons.length) * 100);
            return {{ percent, completedCount: done, totalCount: lessons.length }};
        }}

        function openLessonPage(courseCode, pageNumber) {{
            const baseBookUrl = BOOK_URLS[courseCode] || BOOK_URLS["ريض 366"];
            const url = baseBookUrl + "#p=" + pageNumber;
            window.open(url, '_blank');
        }}

        function toggleLessonCheck(lessonId, chapterId) {{
            const key = 'mathrise_lesson_' + lessonId;
            const current = localStorage.getItem(key) === 'true';
            localStorage.setItem(key, (!current).toString());

            renderLessonsModal(chapterId);
            renderCoursesView(currentActiveStage);
        }}

        function openChapterLessonsModal(chapterId) {{
            let targetTopic = null;
            let targetCourse = null;

            const list = coursesData[currentActiveStage] || [];
            list.forEach(c => {{
                c.topics.forEach(t => {{
                    if (t.id === chapterId) {{
                        targetTopic = t;
                        targetCourse = c;
                    }}
                }});
            }});

            if (!targetTopic) return;

            renderLessonsModal(chapterId);
            document.getElementById('detailsModal').style.display = 'flex';
        }}

        function renderLessonsModal(chapterId) {{
            let targetTopic = null;
            let targetCourse = null;

            const list = coursesData[currentActiveStage] || [];
            list.forEach(c => {{
                c.topics.forEach(t => {{
                    if (t.id === chapterId) {{
                        targetTopic = t;
                        targetCourse = c;
                    }}
                }});
            }});

            if (!targetTopic) return;

            const prog = calculateTopicProgress(targetTopic.lessons);
            document.getElementById('modalCourseTitle').innerHTML = `
                <div style="display: flex; align-items: center; gap: 10px;">
                    <i class="fas fa-book" style="color: #5D45FD; font-size: 1.3rem;"></i>
                    <span>فصل ${{targetTopic.title}} (${{targetCourse.code}})</span>
                </div>
            `;

            let lessonsHTML = '';
            targetTopic.lessons.forEach((ls, idx) => {{
                const isDone = localStorage.getItem('mathrise_lesson_' + ls.id) === 'true';
                const rowClass = isDone ? 'lesson-row is-done' : 'lesson-row';
                const checkBtnClass = isDone ? 'lesson-check-btn checked' : 'lesson-check-btn';
                const checkIcon = isDone ? '<i class="fas fa-check"></i>' : '';

                lessonsHTML += `
                    <div class="${{rowClass}}">
                        <div class="lesson-info">
                            <button class="${{checkBtnClass}}" title="تحديد كمنجز" onclick="toggleLessonCheck('${{ls.id}}', '${{chapterId}}')">
                                ${{checkIcon}}
                            </button>
                            <span class="lesson-name">${{ls.title}}</span>
                        </div>
                        <button class="open-lesson-btn" onclick="openLessonPage('${{targetCourse.code}}', ${{ls.page}})" title="فتح صفحة هذا الدرس في الكتاب">
                            <i class="fas fa-book-open"></i> صفحة ${{ls.page}}
                        </button>
                    </div>
                `;
            }});

            document.getElementById('modalCourseBody').innerHTML = `
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; padding: 0 4px;">
                    <span style="font-size: 0.9rem; font-weight: 700; color: #475569;">نسبة إنجازك في هذا الفصل:</span>
                    <span style="font-size: 1rem; font-weight: 800; color: ${{prog.percent === 100 ? '#10B981' : '#5D45FD'}};">
                        ${{prog.percent}}% (${{prog.completedCount}} من ${{prog.totalCount}} دروس)
                    </span>
                </div>
                <div style="width: 100%; height: 8px; background: #E2E8F0; border-radius: 8px; overflow: hidden; margin-bottom: 20px;">
                    <div style="height: 100%; width: ${{prog.percent}}%; background: ${{prog.percent === 100 ? '#10B981' : '#5D45FD'}}; transition: width 0.3s ease;"></div>
                </div>
                <div class="lessons-list">
                    ${{lessonsHTML}}
                </div>
            `;
        }}

        function renderCoursesView(stageName) {{
            const coursesContent = document.getElementById('coursesContent');
            coursesContent.innerHTML = '';

            const list = coursesData[stageName] || [];
            list.forEach(course => {{
                const singleBlock = document.createElement('div');
                singleBlock.className = 'single-course-block';

                const colsCount = course.topics.length;
                const gridColsClass = colsCount <= 2 ? 'cols-2' : (colsCount === 3 ? 'cols-3' : 'cols-4');

                let topicsHTML = '';
                course.topics.forEach(tp => {{
                    const prog = calculateTopicProgress(tp.lessons);
                    const fillClass = prog.percent === 100 ? 'topic-progress-fill completed' : 'topic-progress-fill';
                    const percentClass = prog.percent === 100 ? 'topic-percent completed' : 'topic-percent';
                    const percentText = prog.percent === 100 ? 'مكتمل ✓' : prog.percent + '%';

                    topicsHTML += `
                        <div class="topic-card" onclick="openChapterLessonsModal('${{tp.id}}')" title="اضغط لعرض دروس هذا الفصل ومتابعة إنجازها 🚀">
                            <div class="topic-icon">${{tp.iconHtml}}</div>
                            <div class="topic-title">${{tp.title}}</div>
                            <div class="topic-progress-bar">
                                <div class="${{fillClass}}" style="width: ${{prog.percent}}%;"></div>
                            </div>
                            <div class="topic-footer">
                                <div class="topic-count"><i class="fas fa-layer-group" style="color: #5D45FD;"></i> ${{tp.lessons.length}} دروس</div>
                                <div class="${{percentClass}}">${{percentText}}</div>
                            </div>
                        </div>
                    `;
                }});

                const quizOnClick = (course.code === "ريض 366") 
                    ? `openQuizConfigModal('${{course.code}}')` 
                    : `alert('بدء الاختبار لمقرر ${{course.code}}')`;

                singleBlock.innerHTML = `
                    <div class="course-code-header">
                        <span><i class="fas fa-book" style="color: #5D45FD;"></i> مقرر ${{course.code}}</span>
                        <span class="chapters-badge"><i class="fas fa-layer-group"></i> ${{course.chaptersCount}} فصول دراسية</span>
                    </div>
                    <div class="course-content-layout">
                        <div class="brief-card">
                            <div>
                                <div class="brief-title">نبذة عن المقرر</div>
                                <div class="brief-text">${{course.brief}}</div>
                            </div>
                            <button class="brief-btn" onclick="openDetailsModal('${{course.code}}', '${{course.details.replace(/'/g, "\\'")}}')">عرض التفاصيل</button>
                        </div>
                        <div class="topics-grid ${{gridColsClass}}">
                            ${{topicsHTML}}
                        </div>
                    </div>

                    <div class="tools-section">
                        <div class="tools-section-title">
                            <i class="fas fa-star"></i> أدواتك في مقرر ${{course.code}}
                        </div>
                        <div class="tools-grid">
                            <div class="tool-card schedule">
                                <div class="tool-icon"><i class="fas fa-calendar-days"></i></div>
                                <div class="tool-title">مواعيد الاختبارات</div>
                                <div class="tool-desc">أضف مواعيد اختباراتك وتصلك تذكيرات قبلها</div>
                                <button class="tool-btn" onclick="openExamsModal('${{course.code}}')">إدارة المواعيد</button>
                            </div>
                            <div class="tool-card grades">
                                <div class="tool-icon"><i class="fas fa-chart-simple"></i></div>
                                <div class="tool-title">درجاتي</div>
                                <div class="tool-desc">تابع درجاتك وتفاصيلك في الاختبارات والواجبات</div>
                                <button class="tool-btn" onclick="openGradesModal('${{course.code}}')">عرض الدرجات</button>
                            </div>
                            <div class="tool-card ai">
                                <div class="tool-icon"><i class="fas fa-robot"></i></div>
                                <div class="tool-title">AI Math Tutor</div>
                                <div class="tool-desc">مساعدك الذكي لفهم الرياضيات وتبسيطها</div>
                                <button class="tool-btn" onclick="openAiTutorModal('${{course.code}}')">اسأل الآن</button>
                            </div>
                            <div class="tool-card quiz">
                                <div class="tool-icon"><i class="fas fa-list-check"></i></div>
                                <div class="tool-title">اختبر نفسك</div>
                                <div class="tool-desc">اختبارات على الدروس والوحدات أو اختبار شامل للمقرر</div>
                                <button class="tool-btn" onclick="${{quizOnClick}}">ابدا اختبار</button>
                            </div>
                            <div class="tool-card notes">
                                <div class="tool-icon"><i class="fas fa-file-signature"></i></div>
                                <div class="tool-title">نوتاتي</div>
                                <div class="tool-desc">ارفع نوتاتك وملفاتك الخاصة بكل درس واحتفظ بها</div>
                                <button class="tool-btn" onclick="openNotesModal('${{course.code}}')">فتح</button>
                            </div>
                        </div>
                    </div>
                `;
                coursesContent.appendChild(singleBlock);
            }});
        }}

        function showCourses(stageName) {{
            currentActiveStage = stageName;
            document.getElementById('stagesView').style.display = 'none';
            const coursesView = document.getElementById('coursesView');
            const currentStageTitle = document.getElementById('currentStageTitle');

            currentStageTitle.innerText = stageName;
            renderCoursesView(stageName);
            coursesView.style.display = 'flex';
        }}

        function showStages() {{
            document.getElementById('coursesView').style.display = 'none';
            document.getElementById('stagesView').style.display = 'block';
        }}

        function openDetailsModal(title, details) {{
            document.getElementById('modalCourseTitle').innerText = 'تفاصيل ' + title;
            document.getElementById('modalCourseBody').innerHTML = `
                <div class="modal-body" style="line-height: 1.8; color: #475569; margin-bottom: 20px;">${{details}}</div>
                <button class="brief-btn" onclick="closeModal()">إغلاق</button>
            `;
            document.getElementById('detailsModal').style.display = 'flex';
        }}

        function getGradesStorage(courseCode) {{
            const raw = localStorage.getItem('mathrise_dynamic_grades_' + courseCode);
            return raw ? JSON.parse(raw) : [];
        }}

        function saveGradesStorage(courseCode, list) {{
            localStorage.setItem('mathrise_dynamic_grades_' + courseCode, JSON.stringify(list));
        }}

        function openGradesModal(courseCode) {{
            document.getElementById('modalCourseTitle').innerHTML = `<i class="fas fa-chart-simple" style="color: #9333EA;"></i> درجاتي والتقييم الذكي (${{courseCode}})`;
            renderGradesModalContent(courseCode);
            document.getElementById('detailsModal').style.display = 'flex';
        }}

        function renderGradesModalContent(courseCode) {{
            const list = getGradesStorage(courseCode);
            
            let totalScore = 0;
            let totalMax = 0;
            let rowsHTML = '';

            list.forEach((item, idx) => {{
                const s = parseFloat(item.score) || 0;
                const m = parseFloat(item.max) || 1;
                totalScore += s;
                totalMax += m;

                let imgIndicator = '';
                if (item.examImage) {{
                    const mime = item.examMime || 'image/png';
                    const fileUrl = `data:${{mime}};base64,${{item.examImage}}`;
                    imgIndicator = `<a href="${{fileUrl}}" target="_blank" style="color: #10B981; margin-left: 6px; cursor: pointer;" title="اضغط لعرض الملف المرفق"><i class="fas fa-paperclip"></i></a>`;
                }}

                rowsHTML += `
                    <div style="display: flex; align-items: center; gap: 8px; background: #FAF5FF; padding: 10px 12px; border-radius: 12px; border: 1.5px solid #E9D5FF; margin-bottom: 8px; direction: rtl;">
                        <input type="text" value="${{item.title}}" placeholder="اسم التقييم" style="flex: 2; padding: 6px 10px; border-radius: 8px; border: 1.5px solid #D8B4FE; font-size: 0.88rem; outline: none; text-align: right;" onchange="editGradeItem('${{courseCode}}', ${{idx}}, 'title', this.value)">
                        ${{imgIndicator}}
                        <input type="number" step="0.5" value="${{item.score}}" placeholder="درجتك" style="width: 65px; padding: 6px 6px; border-radius: 8px; border: 1.5px solid #D8B4FE; text-align: center; font-weight: 700; outline: none;" onchange="editGradeItem('${{courseCode}}', ${{idx}}, 'score', this.value)">
                        <span style="font-weight: 700; color: #9333EA;">من</span>
                        <input type="number" step="0.5" value="${{item.max}}" placeholder="العظمى" style="width: 65px; padding: 6px 6px; border-radius: 8px; border: 1.5px solid #D8B4FE; text-align: center; font-weight: 700; outline: none;" onchange="editGradeItem('${{courseCode}}', ${{idx}}, 'max', this.value)">
                        <button onclick="deleteGradeItem('${{courseCode}}', ${{idx}})" style="background: #FEE2E2; color: #DC2626; border: none; border-radius: 8px; width: 32px; height: 32px; cursor: pointer;" title="حذف التقييم"><i class="fas fa-trash"></i></button>
                    </div>
                `;
            }});

            const percent = totalMax > 0 ? Math.round((totalScore / totalMax) * 100) : 0;

            let levelTitle = '';
            let feedbackIcon = '';
            let levelDesc = '';

            if (percent < 60) {{
                levelTitle = 'مستوى مبتدئ ';
                feedbackIcon = 'fa-seedling';
                levelDesc = 'تحتاج إلى مضاعفة الجهود ومراجعة أساسيات المقرر بشكل مكثف.';
            }} else if (percent >= 60 && percent < 75) {{
                levelTitle = 'مستوى مقبول ';
                feedbackIcon = 'fa-battery-half';
                levelDesc = 'أداؤك مقبول، ولكنك تحتاج إلى حل المزيد من التمارين لتثبيت المعلومات.';
            }} else if (percent >= 75 && percent < 85) {{
                levelTitle = 'مستوى جيد ';
                feedbackIcon = 'fa-dumbbell';
                levelDesc = 'أداؤك جيد جداً، بقليل من التركيز في التفاصيل ستصل للقمة.';
            }} else if (percent >= 85 && percent < 95) {{
                levelTitle = 'مستوى متقدم ';
                feedbackIcon = 'fa-star';
                levelDesc = 'مستوى متميز ومبهر! لديك استيعاب قوي جداً للمفاهيم الرياضية.';
            }} else {{
                levelTitle = 'مستوى استثنائي ';
                feedbackIcon = 'fa-crown';
                levelDesc = 'أداء كامل واستثنائي! أنت بطل حقيقي في الرياضيات.';
            }}

            let remediationHTML = '';
            if (list.length > 0) {{
                const lastExam = list[list.length - 1];
                if (lastExam.score < lastExam.max && lastExam.customPlan && lastExam.customPlan.trim()) {{
                    remediationHTML = `
                        <div style="margin-top: 12px; border-radius: 16px; padding: 20px; border: 1.5px solid #E0E7FF; background: linear-gradient(135deg, #FAF5FF 0%, #EEF2FF 100%); color: #1E1B4B;">
                            <div style="font-size: 1.05rem; font-weight: 800; display: flex; align-items: center; gap: 8px; margin-bottom: 10px; color: #5D45FD;">
                                <i class="fas fa-bullseye"></i>
                                <span>خطة التطوير المقترحة (${{lastExam.title}}):</span>
                            </div>
                            <div style="font-size: 0.93rem; line-height: 2; text-align: right; color: #334155;">
                                ${{lastExam.customPlan.replace(/\\n/g, ' ')}}
                            </div>
                        </div>
                    `;
                }}
            }}

            document.getElementById('modalCourseBody').innerHTML = `
                <div style="display: flex; flex-direction: column; gap: 14px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                        <span style="font-size: 0.9rem; color: #475569; font-weight: 700;">سجل درجاتك :</span>
                        <button onclick="showManualGradeForm('${{courseCode}}')" style="background: #9333EA; color: white; border: none; padding: 6px 12px; border-radius: 8px; font-weight: 700; font-size: 0.82rem; cursor: pointer;">
                            <i class="fas fa-plus"></i> إضافة تقييم جديد
                        </button>
                    </div>

                    <div id="manualGradeFormContainer" style="display: none; background: #FAF5FF; padding: 16px; border-radius: 18px; border: 1.5px solid #D8B4FE; flex-direction: column; gap: 12px;">
                        <div style="font-weight: 800; color: #7E22CE; font-size: 1rem; text-align: right;">إضافة تقييم جديد:</div>

                        <div style="display: flex; gap: 10px; align-items: center;">
                            <input type="text" id="manualTitleInput" placeholder="اسم التقييم (مثلاً: اختبار التكامل أو الاشتقاق)" class="exam-input" style="flex: 2; padding: 10px 14px; font-size: 0.9rem; text-align: right;">
                            <input type="number" step="0.5" id="manualScoreInput" placeholder="درجتك" class="exam-input" style="width: 90px; padding: 10px 14px; font-size: 0.9rem; text-align: center;">
                            <span style="font-weight: 800; color: #7E22CE; white-space: nowrap;">من</span>
                            <input type="number" step="0.5" id="manualMaxInput" placeholder="العظمى" class="exam-input" style="width: 90px; padding: 10px 14px; font-size: 0.9rem; text-align: center;" value="10">
                        </div>

                        <div style="display: flex; flex-direction: column; gap: 6px; text-align: right;">
                            <label style="font-size: 0.85rem; font-weight: 700; color: #475569; display: flex; align-items: center; gap: 6px; cursor: pointer;" onclick="document.getElementById('manualExamImageInput').click()">
                                <i class="fas fa-paperclip" style="color: #5D45FD; font-size: 1.1rem;"></i> <span>(اختياري) إرفاق ملف أو صورة الاختبار ليتم تحليل خطواتك بدقة</span>
                            </label>
                            <input type="file" id="manualExamImageInput" accept="image/*, application/pdf" style="font-size: 0.85rem; padding: 6px; background: white; border-radius: 8px; border: 1.5px solid #E2E8F0;">
                        </div>

                        <div style="display: flex; gap: 10px; margin-top: 6px;">
                            <button type="button" id="saveManualGradeBtn" onclick="saveManualGrade('${{courseCode}}')" style="background: #10B981; color: white; border: none; padding: 10px 18px; border-radius: 12px; font-weight: 800; cursor: pointer; flex: 1; font-size: 0.95rem;">حفظ</button>
                            <button type="button" onclick="document.getElementById('manualGradeFormContainer').style.display='none'" style="background: #E2E8F0; color: #475569; border: none; padding: 10px 18px; border-radius: 12px; font-weight: 800; cursor: pointer; font-size: 0.95rem;">إلغاء</button>
                        </div>
                    </div>

                    <div style="max-height: 200px; overflow-y: auto;">
                        ${{rowsHTML || '<div style="text-align: center; color: #94A3B8; padding: 15px;">لا توجد تقييمات مسجلة. اضغط على "إضافة تقييم جديد".</div>'}}
                    </div>

                    <div class="stats-summary-card" style="margin-top: 4px; background: #FFFFFF; border: 1.5px solid #E2E8F0; border-radius: 16px; padding: 14px; display: flex; align-items: center; justify-content: space-around;">
                        <div style="text-align: center;">
                            <div style="font-size: 1.3rem; font-weight: 800; color: #9333EA;">${{totalScore.toFixed(1)}} من ${{totalMax.toFixed(1)}}</div>
                            <div style="font-size: 0.8rem; color: #64748B; font-weight: 700;">مجموع الدرجات المحصلة</div>
                        </div>
                        <div style="width: 1.5px; height: 35px; background: #E2E8F0;"></div>
                        <div style="text-align: center;">
                            <div style="font-size: 1.3rem; font-weight: 800; color: ${{percent >= 75 ? '#10B981' : (percent >= 60 ? '#F59E0B' : '#EF4444')}};">${{percent}}%</div>
                            <div style="font-size: 0.8rem; color: #64748B; font-weight: 700;">النسبة المئوية الإجمالية</div>
                        </div>
                    </div>

                    <div style="border-radius: 14px; padding: 16px; border: 1.5px solid #CBD5E1; background: #F8FAFC; color: #1E1B4B;">
                        <div style="font-size: 1rem; font-weight: 800; display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                            <i class="fas ${{feedbackIcon}}" style="color: #9333EA;"></i>
                            <span>تقييم المستوى الدراسي: ${{levelTitle}}</span>
                        </div>
                        <div style="font-size: 0.9rem; color: #475569; line-height: 1.6;">${{levelDesc}}</div>
                    </div>

                    ${{remediationHTML}}
                </div>
            `;
        }}

        function showManualGradeForm(courseCode) {{
            const form = document.getElementById('manualGradeFormContainer');
            if(form) {{
                form.style.display = form.style.display === 'flex' ? 'none' : 'flex';
            }}
        }}

        async function saveManualGrade(courseCode) {{
            if (isSavingManualGrade) return;
            isSavingManualGrade = true;

            const saveBtn = document.getElementById('saveManualGradeBtn');
            const originalBtnText = saveBtn ? saveBtn.innerHTML : '';
            if (saveBtn) {{
                saveBtn.disabled = true;
                saveBtn.style.opacity = '0.7';
                saveBtn.style.cursor = 'not-allowed';
                saveBtn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> جاري التحليل وصياغة الخطة...';
            }}

            try {{
                const title = document.getElementById('manualTitleInput').value.trim() || 'اختبار مدرسي';
                const score = parseFloat(document.getElementById('manualScoreInput').value);
                const max = parseFloat(document.getElementById('manualMaxInput').value);
                const fileInput = document.getElementById('manualExamImageInput');

                if (isNaN(score) || isNaN(max) || max <= 0) {{
                    alert('الرجاء إدخال الدرجة والدرجة العظمى بشكل صحيح.');
                    return;
                }}

                let customPlan = '';
                let base64File = null;
                let fileMime = 'image/png';

                const generateAiPlan = async (fileData, mimeType) => {{
                    let promptParts = [];
                    let promptText = `أنت موجه ومعلم رياضيات خبير لمقرر (${{courseCode}}). 
أجرى الطالب تقييماً بعنوان: "${{title}}"، وحصل على درجة ${{score}} من ${{max}}.
محتوى فصول الكتاب المدرسي المعتمدة:
${{MATH366_BOOK_CONTEXT}}

المطلوب بدقة وأمانة علمية:
1. حلل بدقة عنوان الاختبار "${{title}}" أو الملف المرفق، وحدد الدروس المرتبطة به مع أرقام صفحاتها الحقيقية من المنهج المرفق.
2. إذا كانت الدرجة كاملة (${{score}} == ${{max}}), اجعل remediation_plan نصاً فارغاً "".
3. إذا خسر الطالب درجات (${{score}} < ${{max}}), صغ "خطة التطوير" كفقرة عربية واحدة متماسكة وطبيعية وموجهة للطالب تماماً كالتالي:
- تبدأ بـ: "بناءً على أدائك في الاختبار، تحتاج إلى مراجعة [اسم الدرس أو الدروس] – الصفحة [رقم الصفحة أو الصفحات], مع التركيز على [المهارة المحددة مثل خطوات الحل أو ترتيب قواعد الاشتقاق أو التكامل] والانتباه إلى [المهارات الحسابية أو الإشارات]..."
- تنتهي بـ: "...يُنصح بالتدرب على مسائل مشابهة تجمع بين هذه المهارات للتأكد من إتقانها, ويمكنك الاستعانة بـ AI Math Tutor لشرح المهارات التي تحتاج إلى تحسينها خطوة بخطوة ومساعدتك على التدريب بأسئلة مشابهة. 🌱✨"
4. ممنوع منعاً باتاً ذكر تفاصيل سلم الدرجات أو خصم درجات أو كتابة (الخطوة الأولى / لم يكتب كذا), واجعلها فقرة متصلة بدون أي تعداد نقطي أو أسطر جديدة.

أرجع النتيجة حصراً بصيغة JSON:
{{
  "remediation_plan": "فقرة واحدة متصلة بالكامل"
}}`;
                    
                    if (fileData) {{
                        promptParts = [{{ text: promptText }}, {{ inlineData: {{ mimeType: mimeType, data: fileData }} }}];
                    }} else {{
                        promptParts = [{{ text: promptText }}];
                    }}

                    try {{
                        const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=${{GEMINI_API_KEY}}`, {{
                            method: 'POST',
                            headers: {{ 'Content-Type': 'application/json' }},
                            body: JSON.stringify({{
                                contents: [{{ parts: promptParts }}],
                                generationConfig: {{ responseMimeType: "application/json" }}
                            }})
                        }});
                        const data = await res.json();
                        const parsed = JSON.parse(data.candidates[0].content.parts[0].text);
                        return parsed.remediation_plan || '';
                    }} catch (e) {{
                        console.error(e);
                        return '';
                    }}
                }};

                if (fileInput.files && fileInput.files[0]) {{
                    const file = fileInput.files[0];
                    fileMime = file.type || 'image/png';
                    const reader = new FileReader();

                    await new Promise((resolve) => {{
                        reader.onload = async function(event) {{
                            base64File = event.target.result.split(',')[1];
                            customPlan = await generateAiPlan(base64File, fileMime);
                            resolve();
                        }};
                        reader.readAsDataURL(file);
                    }});
                }} else if (score < max) {{
                    customPlan = await generateAiPlan(null, null);
                }}

                const list = getGradesStorage(courseCode);
                list.push({{
                    title: title,
                    score: score,
                    max: max,
                    customPlan: customPlan,
                    examImage: base64File,
                    examMime: fileMime
                }});
                saveGradesStorage(courseCode, list);
                renderGradesModalContent(courseCode);
                alert("تمت إضافة التقييم وتحليل خطة التطوير بنجاح!");
            }} finally {{
                isSavingManualGrade = false;
                const btnAfter = document.getElementById('saveManualGradeBtn');
                if (btnAfter) {{
                    btnAfter.disabled = false;
                    btnAfter.style.opacity = '1';
                    btnAfter.style.cursor = 'pointer';
                    btnAfter.innerHTML = originalBtnText || 'حفظ';
                }}
            }}
        }}

        function editGradeItem(courseCode, index, field, value) {{
            const list = getGradesStorage(courseCode);
            if (list[index]) {{
                list[index][field] = (field === 'score' || field === 'max') ? (parseFloat(value) || 0) : value;
                saveGradesStorage(courseCode, list);
                renderGradesModalContent(courseCode);
            }}
        }}

        function deleteGradeItem(courseCode, index) {{
            const list = getGradesStorage(courseCode);
            list.splice(index, 1);
            saveGradesStorage(courseCode, list);
            renderGradesModalContent(courseCode);
        }}

        function getExamsStorage(courseCode) {{
            const raw = localStorage.getItem('mathrise_exams_' + courseCode);
            return raw ? JSON.parse(raw) : [];
        }}

        function saveExamsStorage(courseCode, exams) {{
            localStorage.setItem('mathrise_exams_' + courseCode, JSON.stringify(exams));
        }}

        function openExamsModal(courseCode) {{
            document.getElementById('modalCourseTitle').innerHTML = `<i class="fas fa-calendar-check" style="color: #F43F5E;"></i> مواعيد وتذكيرات اختبارات مقرر ${{courseCode}}`;
            renderExamsModalContent(courseCode);
            document.getElementById('detailsModal').style.display = 'flex';
        }}

        function toggleAlarmPicker() {{
            const box = document.getElementById('alarmPickerBox');
            if (box.style.display === 'flex') {{
                box.style.display = 'none';
            }} else {{
                box.style.display = 'flex';
                renderAlarmDial();
            }}
        }}

        function switchPickerMode(mode) {{
            pickerState.mode = mode;
            document.getElementById('alarmHourBtn').classList.toggle('active', mode === 'hours');
            document.getElementById('alarmMinBtn').classList.toggle('active', mode === 'minutes');
            renderAlarmDial();
        }}

        function setAlarmPeriod(period) {{
            pickerState.period = period;
            document.getElementById('periodAmBtn').classList.toggle('active', period === 'AM');
            document.getElementById('periodPmBtn').classList.toggle('active', period === 'PM');
            updateAlarmFieldText();
        }}

        function renderAlarmDial() {{
            const dial = document.getElementById('alarmDialBox');
            dial.innerHTML = '<div class="alarm-center-dot"></div><div class="alarm-hand" id="alarmHand"></div>';

            const isHours = pickerState.mode === 'hours';
            const count = 12;
            const radius = 64;

            for (let i = 1; i <= count; i++) {{
                const val = isHours ? (i < 10 ? '0' + i : '' + i) : ((i * 5) % 60 === 0 ? '00' : ((i * 5) < 10 ? '0' + (i * 5) : '' + (i * 5)));
                const angle = (i * 30) * (Math.PI / 180);
                const x = 85 + radius * Math.sin(angle) - 14;
                const y = 85 - radius * Math.cos(angle) - 14;

                const numEl = document.createElement('div');
                numEl.className = 'alarm-dial-number';
                numEl.style.left = x + 'px';
                numEl.style.top = y + 'px';
                numEl.innerText = val;

                const isSelected = isHours ? pickerState.hour === val : pickerState.minute === val;
                if (isSelected) {{
                    numEl.classList.add('selected');
                    const rotAngle = i * 30;
                    document.getElementById('alarmHand').style.transform = `rotate(${{rotAngle}}deg)`;
                }}

                numEl.onclick = (e) => {{
                    e.stopPropagation();
                    if (isHours) {{
                        pickerState.hour = val;
                        document.getElementById('alarmHourBtn').innerText = val;
                        switchPickerMode('minutes');
                    }} else {{
                        pickerState.minute = val;
                        document.getElementById('alarmMinBtn').innerText = val;
                        renderAlarmDial();
                    }}
                    updateAlarmFieldText();
                }};

                dial.appendChild(numEl);
            }}
        }}

        function updateAlarmFieldText() {{
            const periodAr = pickerState.period === 'AM' ? 'صباحاً' : 'مساءً';
            const formatted = `${{pickerState.hour}}:${{pickerState.minute}} ${{periodAr}}`;
            document.getElementById('alarmTimeDisplay').innerText = formatted;
            document.getElementById('examTimeInput').value = `${{pickerState.hour}}:${{pickerState.minute}} ${{pickerState.period}}`;
        }}

        function confirmAlarmTime() {{
            document.getElementById('alarmPickerBox').style.display = 'none';
        }}

        function renderExamsModalContent(courseCode) {{
            const exams = getExamsStorage(courseCode);
            const today = new Date();
            today.setHours(0, 0, 0, 0);

            let examsHTML = '';
            if (exams.length === 0) {{
                examsHTML = `<div style="text-align: center; color: #94A3B8; padding: 20px; font-size: 0.9rem;">لا توجد أي مواعيد اختبارات مضافة لهذا المقرر حتى الآن.</div>`;
            }} else {{
                exams.sort((a, b) => new Date(a.date) - new Date(b.date));

                exams.forEach((ex, idx) => {{
                    const examDate = new Date(ex.date);
                    examDate.setHours(0, 0, 0, 0);
                    const diffTime = examDate - today;
                    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

                    let badgeClass = 'safe';
                    let badgeText = '';
                    let itemClass = 'exam-item';

                    if (diffDays < 0) {{
                        badgeClass = 'past';
                        badgeText = 'انتهى الاختبار';
                    }} else if (diffDays === 0) {{
                        badgeClass = 'soon';
                        badgeText = '🔔 الاختبار اليوم!';
                        itemClass += ' soon';
                    }} else if (diffDays === 1) {{
                        badgeClass = 'soon';
                        badgeText = '⚡ غداً الاختبار!';
                        itemClass += ' soon';
                    }} else if (diffDays <= 3) {{
                        badgeClass = 'soon';
                        badgeText = `⏳ متبقي ${{diffDays}} أيام`;
                        itemClass += ' soon';
                    }} else {{
                        badgeClass = 'safe';
                        badgeText = `📅 متبقي ${{diffDays}} يوماً`;
                    }}

                    examsHTML += `
                        <div class="${{itemClass}}">
                            <div>
                                <div style="font-weight: 800; color: #1E1B4B; font-size: 1rem; margin-bottom: 4px;">${{ex.title}}</div>
                                <div style="font-size: 0.82rem; color: #64748B; display: flex; align-items: center; gap: 12px;">
                                    <span><i class="far fa-calendar"></i> ${{ex.date}}</span>
                                    <span><i class="far fa-clock"></i> ${{ex.time ? ex.time : 'الوقت غير محدد'}}</span>
                                    <span><i class="fas fa-tag"></i> ${{ex.type}}</span>
                                </div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 12px;">
                                <span class="exam-badge ${{badgeClass}}">${{badgeText}}</span>
                                <button class="delete-note-btn" onclick="deleteExam('${{courseCode}}', ${{idx}})" title="حذف الموعد">
                                    <i class="fas fa-trash"></i>
                                </button>
                            </div>
                        </div>
                    `;
                }});
            }}

            document.getElementById('modalCourseBody').innerHTML = `
                <div class="exam-form-card">
                    <div style="font-weight: 800; color: #9F1239; font-size: 1rem; margin-bottom: 4px; display: flex; align-items: center; gap: 8px;">
                        <i class="fas fa-plus-circle"></i> إضافة موعد اختبار جديد
                    </div>
                    
                    <div class="exam-form-group">
                        <label class="exam-form-label"><i class="fas fa-pen-to-square"></i> اسم الاختبار أو الموضوع المطلـوب:</label>
                        <input type="text" id="examTitleInput" class="exam-input" placeholder="مثال: الفصل الأول">
                    </div>

                    <div class="exam-form-group">
                        <label class="exam-form-label"><i class="fas fa-tag"></i> نوع التقييم:</label>
                        <select id="examTypeInput" class="exam-select">
                            <option value="اختبار قصير (Quiz)">اختبار قصير (Quiz)</option>
                            <option value="اختبار منتصف (Midterm)">اختبار منتصف (Midterm)</option>
                            <option value="اختبار نهائي (Final)">اختبار نهائي (Final)</option>
                            <option value="تطبيق / واجب مهم">تطبيق / واجب مهم</option>
                        </select>
                    </div>

                    <div class="exam-row-two-cols">
                        <div class="exam-form-group">
                            <label class="exam-form-label"><i class="far fa-calendar"></i> التاريخ:</label>
                            <input type="date" id="examDateInput" class="exam-input">
                        </div>
                        
                        <div class="exam-form-group">
                            <label class="exam-form-label"><i class="far fa-clock"></i> الوقت:</label>
                            <input type="hidden" id="examTimeInput" value="08:30 AM">
                            <div class="alarm-time-field" onclick="toggleAlarmPicker()">
                                <span id="alarmTimeDisplay"><i class="fas fa-bell" style="color: #F43F5E;"></i> 08:30 صباحاً</span>
                                <i class="fas fa-clock" style="color: #F43F5E;"></i>
                            </div>

                            <div class="alarm-picker-box" id="alarmPickerBox">
                                <div style="display: flex; align-items: center; justify-content: space-between;">
                                    <span style="font-size: 0.85rem; font-weight: 800; color: #9F1239;"><i class="fas fa-stopwatch"></i> ضبط وقت المنبه</span>
                                    <button onclick="confirmAlarmTime()" style="background: none; border: none; color: #64748B; cursor: pointer;"><i class="fas fa-times"></i></button>
                                </div>
                                <div class="alarm-display-row">
                                    <div class="alarm-num-box active" id="alarmHourBtn" onclick="switchPickerMode('hours')">08</div>
                                    <span style="font-size: 1.6rem; font-weight: 800; color: #E11D48;">:</span>
                                    <div class="alarm-num-box" id="alarmMinBtn" onclick="switchPickerMode('minutes')">30</div>
                                    <div class="alarm-period-toggle">
                                        <button class="alarm-period-btn active" id="periodAmBtn" onclick="setAlarmPeriod('AM')">AM</button>
                                        <button class="alarm-period-btn" id="periodPmBtn" onclick="setAlarmPeriod('PM')">PM</button>
                                    </div>
                                </div>

                                <div class="alarm-dial-container" id="alarmDialBox"></div>

                                <button class="alarm-confirm-btn" onclick="confirmAlarmTime()">
                                    <i class="fas fa-check"></i> تم ضبط الوقت
                                </button>
                            </div>
                        </div>
                    </div>

                    <button class="add-exam-btn" onclick="addExam('${{courseCode}}')">
                        <i class="fas fa-bell"></i> حفظ الموعد وتفعيل التذكير الذكي
                    </button>
                </div>

                <div style="font-weight: 800; color: #1E1B4B; margin-bottom: 12px; font-size: 1rem; display: flex; justify-content: space-between;">
                    <span><i class="fas fa-list-check" style="color: #F43F5E;"></i> قائمة الاختبارات المجدولة (${{exams.length}}):</span>
                </div>
                <div class="exams-list">
                    ${{examsHTML}}
                </div>
            `;
            updateAlarmFieldText();
        }}

        function addExam(courseCode) {{
            const title = document.getElementById('examTitleInput').value.trim();
            const type = document.getElementById('examTypeInput').value;
            const date = document.getElementById('examDateInput').value;
            const time = document.getElementById('examTimeInput').value;

            if (!title || !date) {{
                alert('الرجاء إدخال اسم الاختبار وتاريخه بشكل صحيح.');
                return;
            }}

            const exams = getExamsStorage(courseCode);
            exams.push({{
                title: title,
                type: type,
                date: date,
                time: time
            }});

            saveExamsStorage(courseCode, exams);
            renderExamsModalContent(courseCode);
        }}

        function deleteExam(courseCode, index) {{
            const exams = getExamsStorage(courseCode);
            exams.splice(index, 1);
            saveExamsStorage(courseCode, exams);
            renderExamsModalContent(courseCode);
        }}

        function openNotesModal(courseCode) {{
            if (!uploadedNotesStore[courseCode]) {{
                uploadedNotesStore[courseCode] = [];
            }}
            document.getElementById('modalCourseTitle').innerHTML = `<i class="fas fa-book-bookmark" style="color: #10B981;"></i> دفتر نوتات مقرر ${{courseCode}}`;
            renderNotesModalContent(courseCode);
            document.getElementById('detailsModal').style.display = 'flex';
        }}

        function renderNotesModalContent(courseCode) {{
            const files = uploadedNotesStore[courseCode] || [];
            let filesListHTML = '';
            if (files.length === 0) {{
                filesListHTML = `<div style="text-align: center; color: #94A3B8; padding: 20px; font-size: 0.9rem;">لم تقم برفع أي ملفات أو نوتات بعد لهذا المقرر.</div>`;
            }} else {{
                files.forEach((fileItem, index) => {{
                    let iconClass = 'fa-file-lines';
                    if (fileItem.type.includes('pdf')) iconClass = 'fa-file-pdf text-red-500';
                    else if (fileItem.type.includes('image')) iconClass = 'fa-file-image text-green-500';
                    else if (fileItem.type.includes('word') || fileItem.name.endsWith('.docx')) iconClass = 'fa-file-word text-blue-500';

                    filesListHTML += `
                        <div class="note-item">
                            <div class="note-info">
                                <i class="fas ${{iconClass}}"></i>
                                <div>
                                    <div class="note-name" title="${{fileItem.name}}">${{fileItem.name}}</div>
                                    <div class="note-size">${{fileItem.size}}</div>
                                </div>
                            </div>
                            <div class="note-actions">
                                <a href="${{fileItem.url}}" target="_blank" class="open-note-btn" title="معاينة أو فتح الملف">
                                    <i class="fas fa-arrow-up-right-from-square"></i> فتح
                                </a>
                                <button class="delete-note-btn" onclick="deleteNoteFile('${{courseCode}}', ${{index}})" title="حذف الملف">
                                    <i class="fas fa-trash"></i>
                                </button>
                            </div>
                        </div>
                    `;
                }});
            }}

            document.getElementById('modalCourseBody').innerHTML = `
                <div class="upload-zone" onclick="document.getElementById('noteFileInput').click()">
                    <i class="fas fa-cloud-arrow-up"></i>
                    <h4>اضغط هنا لرفع نوتاتك وملفاتك الخاصة</h4>
                    <p>يدعم ملفات PDF، الصور (JPG, PNG)، ومستندات Word</p>
                    <input type="file" id="noteFileInput" style="display: none;" multiple accept=".pdf, image/*, .docx, .txt" onchange="handleFileUpload(event, '${{courseCode}}')">
                </div>
                <div style="font-weight: 800; color: #1E1B4B; margin-bottom: 12px; font-size: 1rem;">
                    <i class="fas fa-folder-open" style="color: #5D45FD;"></i> نوتاتك المحفوظة (${{files.length}}):
                </div>
                <div class="notes-list">${{filesListHTML}}</div>
            `;
        }}

        function handleFileUpload(event, courseCode) {{
            const selectedFiles = event.target.files;
            if (!selectedFiles || selectedFiles.length === 0) return;

            for (let i = 0; i < selectedFiles.length; i++) {{
                const f = selectedFiles[i];
                const fileSize = (f.size / (1024 * 1024)).toFixed(2) > 0.01 
                    ? (f.size / (1024 * 1024)).toFixed(2) + ' MB' 
                    : (f.size / 1024).toFixed(1) + ' KB';
                const fileUrl = URL.createObjectURL(f);
                uploadedNotesStore[courseCode].push({{
                    name: f.name,
                    size: fileSize,
                    type: f.type,
                    url: fileUrl
                }});
            }}
            renderNotesModalContent(courseCode);
        }}

        function deleteNoteFile(courseCode, index) {{
            const fileItem = uploadedNotesStore[courseCode][index];
            if (fileItem && fileItem.url) {{
                URL.revokeObjectURL(fileItem.url);
            }}
            uploadedNotesStore[courseCode].splice(index, 1);
            renderNotesModalContent(courseCode);
        }}

        function initSpeechRecognition() {{
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!SpeechRecognition) {{
                alert("عذراً، متصفحك لا يدعم الإدخال الصوتي المباشر. يرجى استخدام متصفح Google Chrome أو Microsoft Edge.");
                return null;
            }}
            const rec = new SpeechRecognition();
            rec.lang = 'ar-SA';
            rec.continuous = false;
            rec.interimResults = false;

            rec.onresult = (event) => {{
                const transcript = event.results[0][0].transcript;
                const input = document.getElementById('chatTextInput');
                if (input) {{
                    input.value = (input.value ? input.value + ' ' : '') + transcript;
                    input.focus();
                }}
                stopRecording();
            }};

            rec.onerror = (err) => {{
                console.error("Speech Recognition Error:", err);
                stopRecording();
            }};

            rec.onend = () => {{
                stopRecording();
            }};

            return rec;
        }}

        function toggleVoiceRecording() {{
            if (!recognition) recognition = initSpeechRecognition();
            if (!recognition) return;

            if (isRecording) {{
                recognition.stop();
                stopRecording();
            }} else {{
                try {{
                    recognition.start();
                    isRecording = true;
                    const btn = document.getElementById('voiceRecBtn');
                    if (btn) btn.classList.add('recording');
                }} catch (e) {{
                    stopRecording();
                }}
            }}
        }}

        function stopRecording() {{
            isRecording = false;
            const btn = document.getElementById('voiceRecBtn');
            if (btn) btn.classList.remove('recording');
        }}

        function openAiTutorModal(courseCode) {{
            currentActiveCourse = courseCode;
            document.getElementById('modalCourseTitle').innerHTML = `<i class="fas fa-robot" style="color: #3B82F6;"></i> AI Math Tutor - ${{courseCode}}`;

            chatMessagesHistory = [
                {{
                    role: "model",
                    parts: [{{ text: `أهلاً بك في AI Math Tutor 👋\nأنا هنا عشان أساعدك تفهم ${{courseCode}} بطريقة بسيطة وتفاعلية.\nاكتب سؤالك، وخلنا نفهم الفكرة ونوصل للحل خطوة بخطوة معًا. ✨` }}]
                }}
            ];

            document.getElementById('modalCourseBody').innerHTML = `
                <div class="ai-chat-container">
                    <div class="chat-box" id="chatBox"></div>

                    <div class="board-popup-container" id="boardPopupBox">
                        <div class="board-header-row">
                            <div class="board-title"><i class="fas fa-pen-nib"></i> السبورة التفاعلية (ارسم أو اكتب مسألتك)</div>
                            <button onclick="toggleWhiteboard()" style="background: none; border: none; color: #64748B; cursor: pointer;"><i class="fas fa-times"></i></button>
                        </div>
                        <canvas id="whiteboardCanvas" width="650" height="150"></canvas>
                        <div class="board-actions">
                            <button class="board-action-btn clear" onclick="clearCanvas()"><i class="fas fa-eraser"></i> مسح السبورة</button>
                            <button class="board-action-btn send" onclick="sendBoardDrawing()"><i class="fas fa-paper-plane"></i> إرسال رسمة السبورة للمعلم</button>
                        </div>
                    </div>

                    <div class="pro-math-keyboard" id="proMathKeyboard">
                        <div class="kb-top-bar">
                            <div class="kb-top-bar-title"><i class="fas fa-calculator"></i> لوحة الرموز الرياضية</div>
                            <div class="kb-nav-group">
                                <button type="button" class="kb-nav-btn" onclick="moveCursor(-1)" title="يسار"><i class="fas fa-arrow-left"></i></button>
                                <button type="button" class="kb-nav-btn" onclick="moveCursor(1)" title="يمين"><i class="fas fa-arrow-right"></i></button>
                                <button type="button" class="kb-nav-btn" onclick="insertKeyVal(' ')" title="مسافة"><i class="fas fa-arrows-left-right"></i></button>
                                <button type="button" class="kb-nav-btn" onclick="backspaceMath()" title="مسح"><i class="fas fa-delete-left"></i></button>
                            </div>
                        </div>

                        <div class="kb-category-row">
                            <button type="button" class="kb-category-pill active-pill" id="sub_basic" onclick="switchSubKb('basic', this)">أساسي</button>
                            <button type="button" class="kb-category-pill" id="sub_algebra" onclick="switchSubKb('algebra', this)">جبر</button>
                            <button type="button" class="kb-category-pill" id="sub_explog" onclick="switchSubKb('explog', this)">أسي ولوغاريتم</button>
                            <button type="button" class="kb-category-pill" id="sub_trig" onclick="switchSubKb('trig', this)">مثلثات</button>
                            <button type="button" class="kb-category-pill" id="sub_calc" onclick="switchSubKb('calc', this)">تفاضل وتكامل</button>
                            <button type="button" class="kb-category-pill" id="sub_symbols" onclick="switchSubKb('symbols', this)">رموز</button>
                        </div>

                        <div id="kbContentArea" class="kb-content-area"></div>
                    </div>

                    <div class="chat-input-row">
                        <button class="chat-icon-btn" onclick="toggleProKeyboard()" id="kbToggleBtn" title="لوحة المفاتيح الرياضية">
                            <i class="fas fa-calculator"></i>
                        </button>
                        <button class="chat-icon-btn" onclick="toggleVoiceRecording()" id="voiceRecBtn" title="تسجيل صوتي بالمايكروفون">
                            <i class="fas fa-microphone"></i>
                        </button>
                        <button class="chat-icon-btn" onclick="toggleWhiteboard()" id="boardToggleBtn" title="فتح السبورة التفاعلية للرسم">
                            <i class="fas fa-pen-nib"></i>
                        </button>
                        <button class="chat-icon-btn" onclick="document.getElementById('chatFileUpload').click()" title="إرفاق ملف">
                            <i class="fas fa-paperclip"></i>
                        </button>
                        <input type="file" id="chatFileUpload" accept="image/*, application/pdf" style="display: none;" onchange="handleChatFileUpload(event)">

                        <input type="text" id="chatTextInput" class="chat-text-input" placeholder="اكتب سؤالك ..." onkeypress="if(event.key==='Enter') sendTextMessage()">

                        <button class="chat-send-btn" onclick="sendTextMessage()">
                            <span>إرسال</span> <i class="fas fa-arrow-up"></i>
                        </button>
                    </div>
                </div>
            `;
            document.getElementById('detailsModal').style.display = 'flex';
            renderChatMessages();
            renderSubKb('basic');
            initCanvas();
        }}

        function toggleProKeyboard() {{
            const kb = document.getElementById('proMathKeyboard');
            const btn = document.getElementById('kbToggleBtn');
            if (kb.style.display === 'flex') {{
                kb.style.display = 'none';
                if(btn) btn.classList.remove('active');
            }} else {{
                kb.style.display = 'flex';
                if(btn) btn.classList.add('active');
            }}
        }}

        function toggleQuizKeyboard(qId) {{
            const kb = document.getElementById('quizMathKeyboard_' + qId);
            const btn = document.getElementById('kbToolBtn_' + qId);
            if (kb) {{
                if (kb.style.display === 'flex') {{
                    kb.style.display = 'none';
                    if(btn) btn.classList.remove('active-tool');
                }} else {{
                    kb.style.display = 'flex';
                    if(btn) btn.classList.add('active-tool');
                    const wb = document.getElementById('quizBoardBox_' + qId);
                    const wbBtn = document.getElementById('wbToolBtn_' + qId);
                    if(wb) wb.style.display = 'none';
                    if(wbBtn) wbBtn.classList.remove('active-tool');
                }}
            }}
        }}

        function toggleQuizWhiteboard(qId) {{
            const wb = document.getElementById('quizBoardBox_' + qId);
            const btn = document.getElementById('wbToolBtn_' + qId);
            if (wb) {{
                if (wb.style.display === 'block') {{
                    wb.style.display = 'none';
                    if(btn) btn.classList.remove('active-tool');
                }} else {{
                    wb.style.display = 'block';
                    if(btn) btn.classList.add('active-tool');
                    const kb = document.getElementById('quizMathKeyboard_' + qId);
                    const kbBtn = document.getElementById('kbToolBtn_' + qId);
                    if(kb) kb.style.display = 'none';
                    if(kbBtn) kbBtn.classList.remove('active-tool');
                    
                    initQuizCanvas(qId);
                }}
            }}
        }}

        function switchSubKb(tab, btnEl) {{
            if (btnEl) {{
                const parent = btnEl.parentElement;
                parent.querySelectorAll('.kb-category-pill').forEach(p => p.classList.remove('active-pill'));
                btnEl.classList.add('active-pill');
            }}
            renderSubKb(tab);
        }}

        function renderSubKb(tab) {{
            document.querySelectorAll('.kb-content-area').forEach(area => {{
                area.innerHTML = getSubKbHtml(tab);
            }});
        }}

        function getSubKbHtml(tab) {{
            const KB_LAYOUT = {{
                basic: [
                    ['(', ')', '7', '8', '9'],
                    ['÷', 'a/b', '4', '5', '6'],
                    ['×', '√', '1', '2', '3'],
                    ['−', '%', '0', '.', '='],
                    ['+', 'π', 'x', 'x²', '±']
                ],
                algebra: [
                    ['x', 'y', 'n', 'x²', 'x³'],
                    ['xⁿ', 'x⁻¹', '√x', '∛x', '|x|'],
                    ['(', ')', 'a/b', 'i', 'θ'],
                    ['f(x)', 'g(x)', '=', '≠', '±']
                ],
                explog: [
                    ['eˣ', 'e', 'ln(x)', 'log(x)', 'logₐb'],
                    ['10ˣ', 'x!', 'π', '%', '≈'],
                    ['(', ')', 'x', 'a/b', '=']
                ],
                trig: [
                    ['sin', 'cos', 'tan', 'cot', 'θ'],
                    ['sec', 'csc', '°', 'rad', 'π'],
                    ['sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'cot⁻¹', '('],
                    ['sinh', 'cosh', 'tanh', ')', '=']
                ],
                calc: [
                    ['d/dx', 'd²/dx²', "f'(x)", "f''(x)", 'lim'],
                    ['∫', '∫ₐᵇ', 'dx', 'Δ', '∞'],
                    ['Σ', '∏', '∂', '→', 'e']
                ],
                symbols: [
                    ['≤', '≥', '≠', '≈', '±'],
                    ['∈', '∉', '∩', '∪', '⊂'],
                    ['∞', 'π', 'θ', 'i', '°']
                ]
            }};

            const rows = KB_LAYOUT[tab] || KB_LAYOUT.basic;
            const FUNC_STYLE_KEYS = new Set(['sin','cos','tan','cot','sec','csc','sin⁻¹','cos⁻¹','tan⁻¹','cot⁻¹','sinh','cosh','tanh','ln(x)','log(x)','logₐb',"f'(x)","f''(x)",'lim','f(x)','g(x)','d/dx','d²/dx²']);
            const BARE_FUNC_KEYS = new Set(['sin','cos','tan','cot','sec','csc','sin⁻¹','cos⁻¹','tan⁻¹','cot⁻¹','sinh','cosh','tanh','√']);

            let html = '<div class="kb-grid-layout">';
            rows.forEach(row => {{
                row.forEach(key => {{
                    let cls = 'kb-grid-key';
                    if (/^[0-9.]$/.test(key)) cls += ' number';
                    else if (FUNC_STYLE_KEYS.has(key)) cls += ' func-key';

                    const insertVal = key.replace(/'/g, "\\\\'");
                    if (BARE_FUNC_KEYS.has(key)) {{
                        html += `<button type="button" class="${{cls}}" onclick="insertFuncVal('${{insertVal}}')">${{key}}</button>`;
                    }} else {{
                        html += `<button type="button" class="${{cls}}" onclick="insertKeyVal('${{insertVal}}')">${{key}}</button>`;
                    }}
                }});
            }});
            html += '</div>';
            return html;
        }}

        function insertKeyVal(val) {{
            const input = activeEssayInputId ? document.getElementById(activeEssayInputId) : document.getElementById('chatTextInput');
            if(!input) return;
            const start = input.selectionStart || input.value.length;
            const end = input.selectionEnd || input.value.length;
            const text = input.value;
            input.value = text.substring(0, start) + val + text.substring(end);
            input.focus();
            input.setSelectionRange(start + val.length, start + val.length);
            recordAnswerFromInput(input);
        }}

        function moveCursor(dir) {{
            const input = activeEssayInputId ? document.getElementById(activeEssayInputId) : document.getElementById('chatTextInput');
            if(!input) return;
            input.focus();
            const pos = (input.selectionStart || 0) + dir;
            input.setSelectionRange(pos, pos);
        }}

        function insertFuncVal(name) {{
            const input = activeEssayInputId ? document.getElementById(activeEssayInputId) : document.getElementById('chatTextInput');
            if(!input) return;
            const start = input.selectionStart || input.value.length;
            const end = input.selectionEnd || input.value.length;
            const text = input.value;
            const val = name + '()';
            input.value = text.substring(0, start) + val + text.substring(end);
            input.focus();
            const cursorPos = start + val.length - 1;
            input.setSelectionRange(cursorPos, cursorPos);
            recordAnswerFromInput(input);
        }}

        function backspaceMath() {{
            const input = activeEssayInputId ? document.getElementById(activeEssayInputId) : document.getElementById('chatTextInput');
            if(!input) return;
            const start = input.selectionStart || 0;
            if (start > 0) {{
                input.value = input.value.substring(0, start - 1) + input.value.substring(start);
                input.setSelectionRange(start - 1, start - 1);
            }}
            input.focus();
            recordAnswerFromInput(input);
        }}

        function recordAnswerFromInput(inputEl) {{
            if (inputEl && inputEl.id && inputEl.id.startsWith('essay_input_')) {{
                const qId = inputEl.id.replace('essay_input_', '');
                recordAnswer(qId, inputEl.value);
            }}
        }}

        function toggleWhiteboard() {{
            const box = document.getElementById('boardPopupBox');
            const btn = document.getElementById('boardToggleBtn');
            if(!box) return;
            if (box.style.display === 'block') {{
                box.style.display = 'none';
                if(btn) btn.classList.remove('active');
            }} else {{
                box.style.display = 'block';
                if(btn) btn.classList.add('active');
                initCanvas();
            }}
        }}

        function renderChatMessages() {{
            const chatBox = document.getElementById('chatBox');
            if(!chatBox) return;
            chatBox.innerHTML = '';

            chatMessagesHistory.forEach(msg => {{
                const msgDiv = document.createElement('div');
                msgDiv.className = msg.role === 'user' ? 'chat-msg user' : 'chat-msg bot';

                let textContent = '';
                let imageContent = '';

                msg.parts.forEach(p => {{
                    if (p.text) textContent += p.text;
                    if (p.inlineData) {{
                        if(p.inlineData.mimeType.startsWith('image/')) {{
                            imageContent += `<br><img src="data:${{p.inlineData.mimeType}};base64,${{p.inlineData.data}}" />`;
                        }} else {{
                            imageContent += `<br><div style="font-size:0.85rem; background:rgba(0,0,0,0.05); padding:4px 8px; border-radius:6px; margin-top:4px;"><i class="fas fa-file-pdf"></i> تم إرفاق ملف PDF</div>`;
                        }}
                    }}
                }});

                msgDiv.innerHTML = formatMathText(textContent) + imageContent;
                chatBox.appendChild(msgDiv);
            }});

            chatBox.scrollTop = chatBox.scrollHeight;

            if (window.renderMathInElement) {{
                renderMathInElement(chatBox, {{
                    delimiters: [
                        {{left: "$$", right: "$$", display: true}},
                        {{left: "$", right: "$", display: false}}
                    ],
                    throwOnError: false,
                    strict: false
                }});
            }}
        }}

        async function sendToGeminiTutor(userParts) {{
            chatMessagesHistory.push({{ role: "user", parts: userParts }});
            renderChatMessages();

            const chatBox = document.getElementById('chatBox');
            const loadingMsg = document.createElement('div');
            loadingMsg.className = 'chat-msg bot';
            loadingMsg.id = 'loadingTutorMsg';
            loadingMsg.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> المعلم الذكي يجهز الشرح التفاعلي...';
            chatBox.appendChild(loadingMsg);
            chatBox.scrollTop = chatBox.scrollHeight;

            const systemInstruction =`
1. **الدور والهوية 👩‍🏫:**
أنت مرشد تعليمي متعاون وودود لمقرر ريض 366.
تعتمد على منهجية البنائية التعليمية، وهدفك تسهيل التعلم الحقيقي والفهم العميق لـ "كيف" و"لماذا" من خلال الحوار التفاعلي.

2. **الأسلوب والنبرة 🎯:**
- كن تعاونيًا، مباشرًا، وواضحًا.
- استخدم أسلوبًا طبيعيًا مثل: "دعنا نكتشف..." و"لنجرّب معًا...".
- تجنب الحشو والمجاملات الفارغة والمديح المبالغ فيه.
- ركّز على فهم الطالب وتقدمه.

3. **التوجيه والتعلم 🧭:**
- وجّه الطالب ولا تلقّنه؛ ساعده للوصول إلى الحل بنفسه.
- اشرح الفكرة بوضوح قبل أن تطلب من الطالب التفكير أو الحل.
- اربط السؤال بالدرس الحالي أو بمفهوم من درس سابق إذا كان ذلك يساعد على فهمه.
- استخدم السقالات التعليمية: قسّم المسائل والمفاهيم الصعبة إلى خطوات صغيرة ومترابطة.
- لا تعطِ الحل الكامل مباشرة.
- بعد كل خطوة، أعطِ الطالب فرصة للمحاولة والتفكير.

4. **التعامل مع التعثر 🛑:**
- إذا أخطأ الطالب، وضّح الخطأ وقدم تلميحًا يساعده على التصحيح.
- إذا واجه صعوبة متكررة (2-3 محاولات) أو طلب الحل صراحة، قدّم له تلميحًا مباشرًا أو الخطوة التالية حتى يستمر التعلم.
- لا تجعل الطالب عالقًا بسبب منع الإجابة.

5. **الأسئلة الإرشادية ❓:**
- اختم الرد بسؤال توجيهي واحد مرتبط مباشرة بالخطوة التالية.
- لا تسأل عن معلومة لم يتم شرحها أو مناقشتها بعد.
- تجنب الأسئلة غير الضرورية أو المصطنعة.
- لا تجعل الحوار مجرد سلسلة من الأسئلة؛ يجب أن يحتوي كل رد على شرح مفيد.

6. **اللغة والأسلوب 🧠:**
- أجب بنفس لغة الطالب.
- اجعل الشرح بسيطًا وواضحًا ومناسبًا لمستواه.
- استخدم أمثلة ومعادلات عند الحاجة.
- استخدم الإيموجي المرتبط بالمحتوى التعليمي باعتدال.
- لا تبدأ بعبارات ترحيبية طويلة أو مديح مثل "سؤال ممتاز!".
- ابدأ مباشرة في صلب الموضوع.
- حافظ على سياق الحوار ولا تكرر ما تم شرحه.

7. **المصدر 📚:**
- اعتمد على محتوى كتاب ريض 366 المرفق كمصدر أساسي.
- إذا كان السؤال يعتمد على درس سابق، استخدم المفهوم السابق كما ورد في الكتاب واربطه بالسؤال الحالي.
- لا تضف قوانين أو طرق حل من خارج الكتاب إلا إذا طلب الطالب ذلك صراحة.
- إذا لم تجد المعلومة في المحتوى المتاح، أخبر الطالب بذلك ولا تخمّن.

8. **Learning Mode:**
الهدف هو أن يشارك الطالب في عملية الحل، وليس أن يحصل على الإجابة جاهزة.
في مسائل الحل، لا تعرض جميع الخطوات أو الناتج النهائي في رد واحد.
اشرح خطوة، ثم دع الطالب ينفذ أو يستنتج الخطوة التالية.

9. **التنسيق الرياضي ✏️:**
- استخدم $...$ للمعادلات داخل النص.
- استخدم $$...$$ للمعادلات والخطوات الرياضية المستقلة.

10. **المرجع 📖:**
في نهاية كل رد، اذكر:
📘 المصدر: [اسم الدرس/الفصل] – صفحة [رقم الصفحة]

السياق المتاح من الكتاب:
${{MATH366_BOOK_CONTEXT}}
            `;

            try {{
                const formattedContents = chatMessagesHistory.map(m => ({{
                    role: m.role === 'model' ? 'model' : 'user',
                    parts: m.parts
                }}));

                const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=${{GEMINI_API_KEY}}`, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{
                        contents: formattedContents,
                        systemInstruction: {{ parts: [{{ text: systemInstruction }}] }}
                    }})
                }});

                const data = await response.json();
                if (data.error) throw new Error(data.error.message);

                const aiReply = data.candidates[0].content.parts[0].text;
                chatMessagesHistory.push({{ role: "model", parts: [{{ text: aiReply }}] }});
            }} catch(err) {{
                chatMessagesHistory.push({{ role: "model", parts: [{{ text: `عذراً، حدث خطأ: ${{err.message || 'يرجى التأكد من صلاحية المفتاح'}}` }}] }});
            }} finally {{
                const lEl = document.getElementById('loadingTutorMsg');
                if(lEl) lEl.remove();
                renderChatMessages();
            }}
        }}

        function sendTextMessage() {{
            const input = document.getElementById('chatTextInput');
            const text = input.value.trim();
            if (!text) return;
            input.value = '';
            sendToGeminiTutor([{{ text: text }}]);
        }}

        function sendBoardDrawing() {{
            if (!canvas) return;
            const dataUrl = canvas.toDataURL('image/png');
            const base64Data = dataUrl.split(',')[1];

            if (activeEssayInputId) {{
                const essayInput = document.getElementById(activeEssayInputId);
                if (essayInput) {{
                    essayInput.value += (essayInput.value ? " " : "") + "[تم إرفاق رسمة السبورة التفاعلية]";
                    recordAnswerFromInput(essayInput);
                }}
                const qId = activeEssayInputId.replace('essay_input_', '');
                currentQuizState.studentAnswers[qId] = currentQuizState.studentAnswers[qId] || {{}};
                currentQuizState.studentAnswers[qId].image = base64Data;
                toggleWhiteboard();
                clearCanvas();
                return;
            }}

            sendToGeminiTutor([
                {{ text: "لقد رسمت هذه المسألة / المعادلة على السبورة التفاعلية، اشرحها لي ووجّهني خطوة بخطوة:" }},
                {{ inlineData: {{ mimeType: "image/png", data: base64Data }} }}
            ]);
            clearCanvas();
            toggleWhiteboard();
        }}

        function handleChatFileUpload(event) {{
            const file = event.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = function(e) {{
                const dataUrl = e.target.result;
                const base64Data = dataUrl.split(',')[1];

                if (activeEssayInputId) {{
                    const essayInput = document.getElementById(activeEssayInputId);
                    if (essayInput) {{
                        essayInput.value += (essayInput.value ? " " : "") + `[تم إرفاق الملف: ${{file.name}}]`;
                        recordAnswerFromInput(essayInput);
                    }}
                    const qId = activeEssayInputId.replace('essay_input_', '');
                    currentQuizState.studentAnswers[qId] = currentQuizState.studentAnswers[qId] || {{}};
                    currentQuizState.studentAnswers[qId].image = base64Data;
                    currentQuizState.studentAnswers[qId].mimeType = file.type;
                    return;
                }}

                let promptMsg = "أرفقت صورة هذه المسألة، كيف أبدأ بحلها خطوة بخطوة؟";
                if(file.type === 'application/pdf') {{
                    promptMsg = "أرفقت ملف PDF لمسألة، يرجى قراءة محتواه وتوجيهي في الحل خطوة بخطوة:";
                }}

                sendToGeminiTutor([
                    {{ text: promptMsg }},
                    {{ inlineData: {{ mimeType: file.type, data: base64Data }} }}
                ]);
            }};
            reader.readAsDataURL(file);
        }}

        function closeModal() {{
            stopRecording();
            document.getElementById('detailsModal').style.display = 'none';
        }}

        let isDrawing = false;
        let canvas, ctx;

        function initCanvas() {{
            canvas = document.getElementById('whiteboardCanvas');
            if(!canvas) return;
            ctx = canvas.getContext('2d');
            ctx.lineWidth = 3;
            ctx.lineCap = 'round';
            ctx.strokeStyle = '#1E1B4B';

            canvas.onmousedown = (e) => {{ isDrawing = true; ctx.beginPath(); ctx.moveTo(e.offsetX, e.offsetY); }};
            canvas.onmousemove = (e) => {{ if (isDrawing) {{ ctx.lineTo(e.offsetX, e.offsetY); ctx.stroke(); }} }};
            canvas.onmouseup = () => {{ isDrawing = false; }};

            canvas.ontouchstart = (e) => {{
                e.preventDefault();
                isDrawing = true;
                const rect = canvas.getBoundingClientRect();
                ctx.beginPath();
                ctx.moveTo(e.touches[0].clientX - rect.left, e.touches[0].clientY - rect.top);
            }};
            canvas.ontouchmove = (e) => {{
                e.preventDefault();
                if (isDrawing) {{
                    const rect = canvas.getBoundingClientRect();
                    ctx.lineTo(e.touches[0].clientX - rect.left, e.touches[0].clientY - rect.top);
                    ctx.stroke();
                }}
            }};
            canvas.ontouchend = () => {{ isDrawing = false; }};
        }}

        function initQuizCanvas(qId) {{
            const c = document.getElementById('quizCanvas_' + qId);
            if(!c) return;
            const x = c.getContext('2d');
            x.lineWidth = 3;
            x.lineCap = 'round';
            x.strokeStyle = '#1E1B4B';

            let drawing = false;
            c.onmousedown = (e) => {{ drawing = true; x.beginPath(); x.moveTo(e.offsetX, e.offsetY); }};
            c.onmousemove = (e) => {{ if (drawing) {{ x.lineTo(e.offsetX, e.offsetY); x.stroke(); }} }};
            c.onmouseup = () => {{ drawing = false; }};
        }}

        function clearCanvas() {{
            if(ctx && canvas) {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
            }}
        }}

        function clearQuizCanvas(qId) {{
            const c = document.getElementById('quizCanvas_' + qId);
            if(c) {{
                const x = c.getContext('2d');
                x.clearRect(0, 0, c.width, c.height);
            }}
        }}

        function sendQuizBoardDrawing(qId) {{
            const c = document.getElementById('quizCanvas_' + qId);
            if(!c) return;
            const dataUrl = c.toDataURL('image/png');
            const base64Data = dataUrl.split(',')[1];

            const essayInput = document.getElementById('essay_input_' + qId);
            if (essayInput) {{
                essayInput.value += (essayInput.value ? " " : "") + "[تم إرفاق رسمة السبورة]";
                recordAnswerFromInput(essayInput);
            }}
            currentQuizState.studentAnswers[qId] = currentQuizState.studentAnswers[qId] || {{}};
            currentQuizState.studentAnswers[qId].image = base64Data;
            toggleQuizWhiteboard(qId);
        }}

        function formatMathText(rawText) {{
            if (!rawText) return '';
            let t = String(rawText)
                .replace(/\\n/g, '<br>')
                .replace(/•/g, '<br>•')
                .replace(/1\./g, '<br>1.')
                .replace(/2\./g, '<br>2.')
                .replace(/3\./g, '<br>3.')
                .replace(/4\./g, '<br>4.');
            return t;
        }}

        function ensureMathDelimiters(text) {{
            if (!text) return '';
            let trimmed = String(text).trim();
            if (trimmed.startsWith('$') && trimmed.endsWith('$')) {{
                return trimmed;
            }}
            return `$${{trimmed}}$`;
        }}

        function openQuizConfigModal(courseCode) {{
            currentQuizState.courseCode = courseCode;
            currentQuizState.scope = 'all';
            currentQuizState.selectedTopics = [];
            currentQuizState.qType = 'mix';
            currentQuizState.numQuestions = 3;
            currentQuizState.studentAnswers = {{}};
            currentQuizState.evaluationResults = null;

            const course = (coursesData[currentActiveStage] || []).find(c => c.code === courseCode);
            const topicsList = course ? course.topics : [];

            document.getElementById('modalCourseTitle').innerHTML = `<i class="fas fa-list-check" style="color: #F59E0B;"></i> اختبر نفسك - ${{courseCode}}`;

            let topicsCheckboxesHTML = '';
            topicsList.forEach(t => {{
                let lessonsSubHTML = '';
                let lessonTitles = [];
                if (t.lessons && t.lessons.length > 0) {{
                    t.lessons.forEach(ls => {{
                        lessonTitles.push(ls.title);
                        lessonsSubHTML += `
                            <label style="display: flex; align-items: center; gap: 8px; font-size: 0.85rem; color: #475569; cursor: pointer; margin-right: 15px; margin-top: 4px;">
                                <input type="checkbox" class="lesson-chk-${{t.id}}" value="${{ls.title}}" onchange="toggleTopicSelect(this)">
                                <span>${{ls.title}}</span>
                            </label>
                        `;
                    }});
                }}

                topicsCheckboxesHTML += `
                    <div style="margin-bottom: 12px; background: #F8FAFC; padding: 10px; border-radius: 12px; border: 1.5px solid #E2E8F0;">
                        <label style="font-weight: 800; font-size: 0.9rem; color: #1E1B4B; display: flex; align-items: center; gap: 8px; cursor: pointer;">
                            <input type="checkbox" data-chapter-id="${{t.id}}" data-lessons='${{JSON.stringify(lessonTitles)}}' onchange="toggleChapterSelect(this)">
                            <span>📁 ${{t.title}} (تحديد الفصل كاملاً)</span>
                        </label>
                        <div style="margin-top: 6px;">${{lessonsSubHTML}}</div>
                    </div>
                `;
            }});

            document.getElementById('modalCourseBody').innerHTML = `
                <div class="quiz-config-card">
                    <div style="font-weight: 800; color: #B45309; font-size: 1.1rem;">🎯 حدد إعدادات الاختبار:</div>

                    <div>
                        <div style="font-weight: 700; color: #1E1B4B; margin-bottom: 8px; font-size: 0.92rem;">1. نطاق الأسئلة:</div>
                        <div class="quiz-option-row">
                            <div class="quiz-radio-label active" id="scopeAllBtn" onclick="setQuizScope('all')">شامل كامل المقرر</div>
                            <div class="quiz-radio-label" id="scopeCustomBtn" onclick="setQuizScope('custom')">دروس محددة</div>
                        </div>
                    </div>

                    <div id="topicsSelectorBox" style="display: none; background: white; padding: 14px; border-radius: 14px; border: 1.5px solid #E2E8F0; flex-direction: column; gap: 10px; max-height: 240px; overflow-y: auto;">
                        <div style="font-size: 0.88rem; font-weight: 800; color:#1E1B4B;">اختر الفصول أو الدروس المطلوبة للاختبار:</div>
                        ${{topicsCheckboxesHTML}}
                    </div>

                    <div>
                        <div style="font-weight: 700; color: #1E1B4B; margin-bottom: 8px; font-size: 0.92rem;">2. نوع الأسئلة:</div>
                        <div class="quiz-option-row">
                            <div class="quiz-radio-label active" id="typeMixBtn" onclick="setQuizType('mix')">متنوع (اختياري + مقالي)</div>
                            <div class="quiz-radio-label" id="typeMcqBtn" onclick="setQuizType('mcq')">اختيار من متعدد فقط</div>
                            <div class="quiz-radio-label" id="typeEssayBtn" onclick="setQuizType('essay')">كتابي (مقالي) فقط</div>
                        </div>
                    </div>

                    <div>
                        <div style="display: flex; justify-content: space-between; font-weight: 700; color: #1E1B4B; margin-bottom: 6px; font-size: 0.92rem;">
                            <span>3. عدد الأسئلة:</span>
                            <span id="numQuestionsDisplay" style="color: #F59E0B; font-weight: 800;">3 أسئلة</span>
                        </div>
                        <input type="range" min="1" max="20" value="3" style="width: 100%; accent-color: #F59E0B;" oninput="setNumQuestions(this.value)">
                    </div>

                    <button class="brief-btn" style="background: #F59E0B; padding: 12px; font-size: 1rem;" onclick="generateQuizViaAI()">
                        <i class="fas fa-play"></i> بدء وإنشاء الاختبار الآن
                    </button>
                </div>
            `;

            document.getElementById('detailsModal').style.display = 'flex';
        }}

        function setQuizScope(scope) {{
            currentQuizState.scope = scope;
            document.getElementById('scopeAllBtn').classList.toggle('active', scope === 'all');
            document.getElementById('scopeCustomBtn').classList.toggle('active', scope === 'custom');
            document.getElementById('topicsSelectorBox').style.display = scope === 'custom' ? 'flex' : 'none';
        }}

        function toggleChapterSelect(chapterCheckbox) {{
            const chapterId = chapterCheckbox.getAttribute('data-chapter-id');
            const lessons = JSON.parse(chapterCheckbox.getAttribute('data-lessons') || '[]');
            const lessonCheckboxes = document.querySelectorAll('.lesson-chk-' + chapterId);

            lessonCheckboxes.forEach(chk => {{
                chk.checked = chapterCheckbox.checked;
                if (chapterCheckbox.checked) {{
                    if (!currentQuizState.selectedTopics.includes(chk.value)) {{
                        currentQuizState.selectedTopics.push(chk.value);
                    }}
                }} else {{
                    currentQuizState.selectedTopics = currentQuizState.selectedTopics.filter(t => t !== chk.value);
                }}
            }});
        }}

        function toggleTopicSelect(checkbox) {{
            if (checkbox.checked) {{
                if (!currentQuizState.selectedTopics.includes(checkbox.value)) {{
                    currentQuizState.selectedTopics.push(checkbox.value);
                }}
            }} else {{
                currentQuizState.selectedTopics = currentQuizState.selectedTopics.filter(t => t !== checkbox.value);
            }}
        }}

        function setQuizType(type) {{
            currentQuizState.qType = type;
            document.getElementById('typeMixBtn').classList.toggle('active', type === 'mix');
            document.getElementById('typeMcqBtn').classList.toggle('active', type === 'mcq');
            document.getElementById('typeEssayBtn').classList.toggle('active', type === 'essay');
        }}

        function setNumQuestions(val) {{
            currentQuizState.numQuestions = val;
            document.getElementById('numQuestionsDisplay').innerText = val + ' أسئلة';
        }}

        async function generateQuizViaAI() {{
            const modalBody = document.getElementById('modalCourseBody');
            modalBody.innerHTML = `
                <div style="text-align: center; padding: 40px 20px;">
                    <i class="fas fa-spinner fa-spin" style="font-size: 2.5rem; color: #F59E0B; margin-bottom: 15px;"></i>
                    <div style="font-weight: 800; font-size: 1.1rem; color: #1E1B4B;">جاري تجهيز اختبارك الذكي...</div>
                    <p style="color: #64748B; font-size: 0.88rem; margin-top: 6px;">نجهّز لك أسئلة مناسبة من الامتحانات السابقة 🎯</p>
                </div>
            `;

            if (!GEMINI_API_KEY) {{
                modalBody.innerHTML = `
                    <div style="text-align: center; color: #DC2626; padding: 20px;">
                        <i class="fas fa-circle-exclamation" style="font-size: 2rem; margin-bottom: 10px;"></i>
                        <div style="font-weight: 700;">لم يتم العثور على مفتاح الـ API داخل ملف env!</div>
                    </div>
                `;
                return;
            }}

            const topicContext = currentQuizState.scope === 'all' ? 'شامل لجميع مواضيع المقرر' : `محدد في الدروس التالية: ${{currentQuizState.selectedTopics.join(', ')}}`;

            const prompt = `
            انت مسؤول عن اختيار وتجميع أسئلة الامتحانات لمقرر الرياضيات (${{currentQuizState.courseCode}}).
            لديك بنك الأسئلة للامتحانات السابقة (المستخرج من ملفات math366_bank.json) التالي:
            ${{JSON.stringify(QUESTIONS_BANK)}}

            المطلوب بدقة وأمانة علمية:
            اختر بالضبط ${{currentQuizState.numQuestions}} أسئلة من بنك الأسئلة المرفق (${{topicContext}}).
            نوع الأسئلة المطلوب: ${{currentQuizState.qType}}.

            ⚠️ شروط صارمة جداً:
            1. انسخ نص كل سؤال حرفياً (Copy-Paste) من بنك الأسئلة دون أي تأليف أو تغيير في الأرقام أو الصياغة أو الرموز.
            2. انسخ نموذج الإجابة الرسمي solution_steps حرفياً سطر بسطر مع توزيع الدرجات كما ورد في الملف لكل خطوة وضعه في model_answer.
            3. حدد درجات السؤال points (تناسب حجم السؤال مثلاً من 5 إلى 10 درجات لكل سؤال بحسب سياق الامتحانات السابقة).
            4. تأكد من أن كل صيغة رياضية في السؤال وفي خيارات options وفي نموذج الإجابة محاطة بعلامات $...$ لتظهر كرموز رياضية صحيحة في KaTeX وليس كنصوص كودية.

            أرجع النتيجة بصيغة JSON فقط كقائمة:
            [
              {{
                "id": 1,
                "type": "mcq أو essay",
                "question": "نص المسألة الأصلي مع الرموز داخل $...$",
                "options": ["$A$", "$B$", "$C$", "$D$"],
                "points": 5,
                "model_answer": "خطوات الحل الرسمية وسلم توزيع الدرجات بالتفصيل سطر بسطر"
              }}
            ]
            `;

            try {{
                const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=${{GEMINI_API_KEY}}`, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{
                        contents: [{{ parts: [{{ text: prompt }}] }}],
                        generationConfig: {{ responseMimeType: "application/json" }}
                    }})
                }});

                const data = await res.json();
                if (data.error) throw new Error(data.error.message);

                const text = data.candidates[0].content.parts[0].text;
                currentQuizState.questions = JSON.parse(text);
                renderQuizTakingScreen();
            }} catch (err) {{
                modalBody.innerHTML = `
                    <div style="text-align: center; color: #DC2626; padding: 20px;">
                        <i class="fas fa-circle-exclamation" style="font-size: 2rem; margin-bottom: 10px;"></i>
                        <div style="font-weight: 700;">تعذر توليد الاختبار:</div>
                        <div style="font-size: 0.85rem; margin-top: 6px; direction: ltr;">${{err.message || 'خطأ في الاتصال'}}</div>
                    </div>
                `;
            }}
        }}

        function renderQuizTakingScreen() {{
            const modalBody = document.getElementById('modalCourseBody');
            let questionsHTML = '';

            currentQuizState.questions.forEach((q, idx) => {{
                let inputArea = '';
                if (q.type === 'mcq' && q.options) {{
                    inputArea = q.options.map((opt) => {{
                        const mathFormattedOpt = ensureMathDelimiters(opt);
                        const cleanValue = opt.replace(/"/g, '&quot;');
                        return `
                            <label class="quiz-mcq-opt">
                                <input type="radio" name="q_${{q.id}}" value="${{cleanValue}}" onchange="recordAnswer(${{q.id}}, this.value)" style="width: 18px; height: 18px; accent-color: #5D45FD; cursor: pointer;">
                                <span class="math-box" style="font-size: 1.1rem; color: #1E1B4B; direction: ltr;">${{mathFormattedOpt}}</span>
                            </label>
                        `;
                    }}).join('');
                }} else {{
                    const essayInputId = `essay_input_${{q.id}}`;
                    inputArea = `
                        <div style="display: flex; flex-direction: column; gap: 8px;">
                            <div style="display: flex; gap: 8px; align-items: center; background: #F8FAFC; padding: 8px 12px; border-radius: 12px; border: 1.5px solid #CBD5E1;">
                                <button type="button" id="kbToolBtn_${{q.id}}" class="kb-tab-pill" onclick="toggleQuizKeyboard(${{q.id}})" title="لوحة المفاتيح الرياضية"><i class="fas fa-calculator" style="color: #5D45FD;"></i> لوحة المفاتيح الرياضية</button>
                                <button type="button" id="wbToolBtn_${{q.id}}" class="kb-tab-pill" onclick="toggleQuizWhiteboard(${{q.id}})" title="السبورة البيضاء"><i class="fas fa-pen-nib" style="color: #10B981;"></i> السبورة التفاعلية</button>
                                <button type="button" class="kb-tab-pill" onclick="document.getElementById('essayFile_${{q.id}}').click();" title="إرفاق صورة أو ملف"><i class="fas fa-paperclip" style="color: #F59E0B;"></i> إرفاق صورة/ملف</button>
                                <input type="file" id="essayFile_${{q.id}}" accept="image/*, application/pdf" style="display: none;" onchange="activeEssayInputId='${{essayInputId}}'; handleChatFileUpload(event)">
                            </div>

                            <div id="quizMathKeyboard_${{q.id}}" class="pro-math-keyboard" style="display: none; margin-bottom: 8px;">
                                <div class="kb-top-bar">
                                    <div class="kb-top-bar-title"><i class="fas fa-calculator"></i> لوحة الرموز الرياضية</div>
                                    <div class="kb-nav-group">
                                        <button type="button" class="kb-nav-btn" onclick="activeEssayInputId='${{essayInputId}}'; moveCursor(-1)"><i class="fas fa-arrow-left"></i></button>
                                        <button type="button" class="kb-nav-btn" onclick="activeEssayInputId='${{essayInputId}}'; moveCursor(1)"><i class="fas fa-arrow-right"></i></button>
                                        <button type="button" class="kb-nav-btn" onclick="activeEssayInputId='${{essayInputId}}'; insertKeyVal(' ')"><i class="fas fa-arrows-left-right"></i></button>
                                        <button type="button" class="kb-nav-btn" onclick="activeEssayInputId='${{essayInputId}}'; backspaceMath()"><i class="fas fa-delete-left"></i></button>
                                    </div>
                                </div>
                                <div class="kb-category-row">
                                    <button type="button" class="kb-category-pill active-pill" onclick="activeEssayInputId='${{essayInputId}}'; switchSubKb('basic', this)">أساسي</button>
                                    <button type="button" class="kb-category-pill" onclick="activeEssayInputId='${{essayInputId}}'; switchSubKb('algebra', this)">جبر</button>
                                    <button type="button" class="kb-category-pill" onclick="activeEssayInputId='${{essayInputId}}'; switchSubKb('explog', this)">أسي ولوغاريتم</button>
                                    <button type="button" class="kb-category-pill" onclick="activeEssayInputId='${{essayInputId}}'; switchSubKb('trig', this)">مثلثات</button>
                                    <button type="button" class="kb-category-pill" onclick="activeEssayInputId='${{essayInputId}}'; switchSubKb('calc', this)">تفاضل وتكامل</button>
                                    <button type="button" class="kb-category-pill" onclick="activeEssayInputId='${{essayInputId}}'; switchSubKb('symbols', this)">رموز</button>
                                </div>
                                <div class="kb-content-area"></div>
                            </div>

                            <div id="quizBoardBox_${{q.id}}" class="board-popup-container" style="display: none; margin-bottom: 8px;">
                                <div class="board-header-row">
                                    <div class="board-title"><i class="fas fa-pen-nib"></i> سبورة السؤال ${{q.id}}</div>
                                    <button type="button" onclick="toggleQuizWhiteboard(${{q.id}})" style="background: none; border: none; color: #64748B; cursor: pointer;"><i class="fas fa-times"></i></button>
                                </div>
                                <canvas id="quizCanvas_${{q.id}}" width="600" height="140"></canvas>
                                <div class="board-actions">
                                    <button type="button" class="board-action-btn clear" onclick="clearQuizCanvas(${{q.id}})"><i class="fas fa-eraser"></i> مسح</button>
                                    <button type="button" class="board-action-btn send" onclick="activeEssayInputId='${{essayInputId}}'; sendQuizBoardDrawing(${{q.id}})"><i class="fas fa-check"></i> اعتماد الرسمة</button>
                                </div>
                            </div>

                            <textarea id="${{essayInputId}}" class="exam-input" rows="3" placeholder="اكتب خطوات الحل أو استخدم الأدوات أعلاه..." onfocus="activeEssayInputId='${{essayInputId}}'" oninput="recordAnswerFromInput(this)"></textarea>
                        </div>
                    `;
                }}

                questionsHTML += `
                    <div class="quiz-question-box">
                        <div style="display: flex; justify-content: space-between; font-weight: 800; color: #1E1B4B; margin-bottom: 10px;">
                            <span>السؤال ${{idx + 1}}</span>
                            <span style="background: #FEF3C7; color: #B45309; padding: 2px 10px; border-radius: 8px; font-size: 0.85rem;">${{q.points}} درجات</span>
                        </div>
                        <div style="font-size: 1.05rem; line-height: 2; margin-bottom: 14px; color: #1E1B4B; text-align: right; direction: rtl;">
                            ${{formatMathText(q.question)}}
                        </div>
                        <div style="display: flex; flex-direction: column; gap: 8px;">${{inputArea}}</div>
                    </div>
                `;
            }});

            modalBody.innerHTML = `
                <div style="display: flex; flex-direction: column; gap: 10px;">
                    ${{questionsHTML}}
                    <button class="brief-btn" style="background: #10B981; padding: 12px; font-size: 1rem; margin-top: 10px;" onclick="submitAndGradeQuiz()">
                        <i class="fas fa-paper-plane"></i> تسليم الاختبار وتصحيحه فورياً
                    </button>
                </div>
            `;

            setTimeout(() => {{
                renderSubKb('basic');
                currentQuizState.questions.forEach(q => {{
                    if (q.type !== 'mcq') {{
                        initQuizCanvas(q.id);
                    }}
                }});
                if (window.renderMathInElement) {{
                    renderMathInElement(modalBody, {{
                        delimiters: [
                            {{left: "$$", right: "$$", display: true}},
                            {{left: "$", right: "$", display: false}}
                        ],
                        throwOnError: false,
                        strict: false
                    }});
                }}
            }}, 50);
        }}

        function recordAnswer(qId, val) {{
            currentQuizState.studentAnswers[qId] = currentQuizState.studentAnswers[qId] || {{}};
            currentQuizState.studentAnswers[qId].text = val;
        }}

        async function submitAndGradeQuiz() {{
            const modalBody = document.getElementById('modalCourseBody');
            modalBody.innerHTML = `
                <div style="text-align: center; padding: 40px 20px;">
                    <i class="fas fa-circle-notch fa-spin" style="font-size: 2.5rem; color: #10B981; margin-bottom: 15px;"></i>
                    <div style="font-weight: 800; font-size: 1.1rem; color: #1E1B4B;">جاري تصحيح إجاباتك بناءً على نموذج الامتحان الوزاري المعتمد ...</div>
                    <p style="color: #64748B; font-size: 0.88rem; margin-top: 6px;">يتم تطبيق معايير التصحيح الوزاري خطوة بخطوة واحتساب الدرجات الجزئية بدقة 📝</p>
                </div>
            `;

            const submissionPayload = currentQuizState.questions.map(q => {{
                const ansObj = currentQuizState.studentAnswers[q.id] || currentQuizState.studentAnswers[`essay_input_${{q.id}}`] || {{ text: "لم يقم الطالب بالإجابة" }};
                return {{
                    id: q.id,
                    type: q.type,
                    question: q.question,
                    points: q.points,
                    model_answer: q.model_answer,
                    student_answer: ansObj.text || "إجابة عبر السبورة أو الملف المرفق",
                    has_image: !!ansObj.image,
                    image_data: ansObj.image || null,
                    mime_type: ansObj.mimeType || "image/png"
                }};
            }});

            const evalPromptText = `أنت مصحح وموجّه رياضيات وزاري دقيق جداً لمقرر (${{currentQuizState.courseCode}}).
بيانات الأسئلة ونموذج الإجابة الرسمي وإجابات الطالب النصية أو صور السبورة:
${{JSON.stringify(submissionPayload)}}
محتوى فصول الكتاب المدرسي المعتمدة:
${{MATH366_BOOK_CONTEXT}}

تعليمات التصحيح الحاسمة:
1. إذا كان السؤال اختيار من متعدد (mcq):
   - قارن إجابة الطالب بإجابة النموذج. إذا كانت صحيحة تماماً اعطِ الدرجة كاملة، وإذا كانت خاطئة اعطِ 0.
   - اكتب في حقل feedback حصراً إما "إجابة صحيحة ✅" أو "إجابة خاطئة ❌. الإجابة الصحيحة هي: [ضع الإجابة الصحيحة هنا]".
2. إذا كان السؤال مقالياً (essay):
   - اكتب كل خطوة في سطر منفصل تماماً (استخدم فواصل الأسطر العادية)، وبحيث تبدأ أسماء الخطوات والدرجات بالعربية بينما تظل الرموز الرياضية الإنجليزية (مثل $x$, $y$, $y'$) مفصولة تماماً ولا تتداخل مع اتجاه النص العربي.
3. صغ "خطة التطوير" في remediation_plan كفقرة عربية واحدة متماسكة وطبيعية وموجهة للطالب (بدون أي تعداد نقطي، وبدون فواصل أسطر، وبدون ترقيم، وبدون عناوين فرعية) تحول الأخطاء الفعلية إلى توصيات تعليمية وتوجهه لاستخدام AI Math Tutor.

أرجع النتيجة بصيغة JSON فقط ككائن:
{{
  "evaluations": [
    {{
      "id": 1,
      "score": 3,
      "feedback": "لأسئلة الدوائر: إجابة صحيحة ✅ / أو للإسئلة المقالية: الخطوة الأولى (...): ...\\nالخطوة الثانية (...): ..."
    }}
  ],
  "remediation_plan": "فقرة واحدة متصلة بالكامل بدون فواصل أسطر"
}}`;

            try {{
                const parts = [{{ text: evalPromptText }}];
                currentQuizState.questions.forEach(q => {{
                    const ansObj = currentQuizState.studentAnswers[q.id] || currentQuizState.studentAnswers[`essay_input_${{q.id}}`];
                    if (ansObj && ansObj.image) {{
                        parts.push({{ inlineData: {{ mimeType: ansObj.mimeType || "image/png", data: ansObj.image }} }});
                    }}
                }});

                const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=${{GEMINI_API_KEY}}`, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{
                        contents: [{{ parts: parts }}],
                        generationConfig: {{ responseMimeType: "application/json" }}
                    }})
                }});

                const data = await res.json();
                if (data.error) throw new Error(data.error.message);

                const parsedData = JSON.parse(data.candidates[0].content.parts[0].text);
                const evalResults = parsedData.evaluations || [];
                currentQuizState.evaluationResults = evalResults;

                let totalEarnedAuto = 0;
                let totalMaxAuto = 0;

                evalResults.forEach(ev => {{
                    const qItem = currentQuizState.questions.find(x => x.id === ev.id);
                    if(qItem) {{
                        const sc = parseFloat(ev.score) || 0;
                        const mx = parseFloat(qItem.points) || 0;
                        totalEarnedAuto += sc;
                        totalMaxAuto += mx;
                    }}
                }});

                let examTitleName = '';
                if (currentQuizState.scope === 'custom' && currentQuizState.selectedTopics.length > 0) {{
                    examTitleName = 'اختبار: ' + currentQuizState.selectedTopics.join(', ');
                }} else {{
                    examTitleName = 'اختبار شامل (' + currentQuizState.courseCode + ')';
                }}

                let existingGrades = getGradesStorage(currentQuizState.courseCode);
                existingGrades.push({{
                    title: examTitleName,
                    score: totalEarnedAuto,
                    max: totalMaxAuto,
                    customPlan: parsedData.remediation_plan || ''
                }});
                saveGradesStorage(currentQuizState.courseCode, existingGrades);

                renderQuizResultsScreen(evalResults);
            }} catch (e) {{
                modalBody.innerHTML = `
                    <div style="text-align: center; color: #DC2626; padding: 20px;">
                        <i class="fas fa-circle-exclamation" style="font-size: 2rem; margin-bottom: 10px;"></i>
                        <div>حدث خطأ أثناء التصحيح: ${{e.message || ''}}</div>
                    </div>
                `;
            }}
        }}

        function renderQuizResultsScreen(evalResults) {{
            const modalBody = document.getElementById('modalCourseBody');

            let totalEarned = 0;
            let totalMax = 0;
            let feedbackCardsHTML = '';

            currentQuizState.questions.forEach(q => {{
                const ev = evalResults.find(r => r.id === q.id) || {{ score: 0, feedback: '' }};
                const earned = parseFloat(ev.score) || 0;
                const maxPts = parseFloat(q.points) || 0;
                totalEarned += earned;
                totalMax += maxPts;

                const ansObj = currentQuizState.studentAnswers[q.id] || currentQuizState.studentAnswers[`essay_input_${{q.id}}`] || {{ text: 'لم تتم الإجابة' }};
                const rawStudentAns = ansObj.text || 'إجابة مرفقة بالسبورة أو بملف';
                const formattedStudentAns = (q.type === 'mcq') ? ensureMathDelimiters(rawStudentAns) : formatMathText(rawStudentAns);
                let imgHtml = ansObj.image ? `<br><img src="data:${{ansObj.mimeType || 'image/png'}};base64,${{ansObj.image}}" style="max-width:200px; border-radius:8px; margin-top:8px; border:1px solid #CBD5E1;" />` : '';

                let formattedModelAnswer = String(q.model_answer || '').split('\\n').join('<br>');
                let formattedFeedback = String(ev.feedback || '').split('\\n').join('<br>');

                feedbackCardsHTML += `
                    <div style="background: #F8FAFC; border: 1.5px solid #E2E8F0; border-radius: 16px; padding: 18px; margin-bottom: 15px;">
                        <div style="display: flex; justify-content: space-between; font-weight: 800; margin-bottom: 8px;">
                            <span style="color: #1E1B4B;">السؤال ${{q.id}}</span>
                            <span style="color: ${{earned === maxPts ? '#10B981' : '#EF4444'}};">درجتك: ${{earned}} من ${{maxPts}}</span>
                        </div>
                        <div style="color: #1E1B4B; font-size: 1rem; line-height: 1.8; margin-bottom: 10px; text-align: right;">${{formatMathText(q.question)}}</div>
                        <div style="background: white; padding: 10px 14px; border-radius: 10px; font-size: 0.92rem; margin-bottom: 10px; border: 1.5px solid #CBD5E1; text-align: right;">
                            <strong>إجابتك:</strong> <span class="math-box">${{formattedStudentAns}}</span>${{imgHtml}}
                        </div>
                        <div style="background: #F0FDF4; border: 1px solid #BBF7D0; color: #166534; padding: 14px; border-radius: 12px; font-size: 0.95rem; margin-bottom: 10px; line-height: 2.2; text-align: right; direction: rtl;">
                            <strong>💡 نموذج الحل :</strong><br>${{formattedModelAnswer}}
                        </div>
                        <div style="font-size: 0.92rem; color: #334155; line-height: 2.2; text-align: right; direction: rtl; background: #FFF; padding: 12px; border-radius: 12px; border: 1px solid #E2E8F0;">
                            <strong>✨ تقييم الحل :</strong><br>${{formattedFeedback}}
                        </div>
                    </div>
                `;
            }});

            modalBody.innerHTML = `
                <div id="printableQuizReport" style="background: #FFFFFF; padding: 25px; border-radius: 16px; direction: rtl;">
                    <div style="text-align: center; margin-bottom: 25px; border-bottom: 2px solid #E2E8F0; padding-bottom: 15px;">
                        <div style="font-size: 1.4rem; font-weight: 800; color: #1E1B4B; margin-bottom: 6px;">تقرير اختبار: ${{currentQuizState.courseCode}}</div>
                        <div style="font-size: 2rem; font-weight: 800; color: #5D45FD; direction: rtl; unicode-bidi: isolate;"><span dir="ltr">${{totalEarned}}</span> من <span dir="ltr">${{totalMax}}</span></div>
                        <div style="font-weight: 700; color: #64748B; font-size: 0.95rem;">الدرجة النهائية في الاختبار</div>
                    </div>
                    <div>${{feedbackCardsHTML}}</div>
                </div>

                <div style="display: flex; gap: 10px; margin-top: 15px;">
                    <button class="brief-btn" style="background: #10B981; flex: 1; display: flex; align-items: center; justify-content: center; gap: 8px;" onclick="downloadQuizPDF()">
                        <i class="fas fa-file-pdf"></i> تحميل تقرير الاختبار كملف PDF
                    </button>
                    <button class="brief-btn" style="background: #5D45FD; flex: 1; display: flex; align-items: center; justify-content: center; gap: 8px;" onclick="openQuizConfigModal('${{currentQuizState.courseCode}}')">
                        <i class="fas fa-rotate-right"></i> إجراء اختبار آخر
                    </button>
                </div>
            `;

            setTimeout(() => {{
                if (window.renderMathInElement) {{
                    renderMathInElement(modalBody, {{
                        delimiters: [
                            {{left: "$$", right: "$$", display: true}},
                            {{left: "$", right: "$", display: false}}
                        ],
                        throwOnError: false,
                        strict: false
                    }});
                }}
            }}, 50);
        }}

        function downloadQuizPDF() {{
            const reportEl = document.getElementById('printableQuizReport');
            if (!reportEl) return;

            const opt = {{
                margin:       [10, 10, 10, 10],
                filename:     `MathRise_${{currentQuizState.courseCode}}_Quiz_Report.pdf`,
                image:        {{ type: 'jpeg', quality: 0.98 }},
                html2canvas:  {{ scale: 2, useCORS: true, logging: true, scrollY: 0 }},
                jsPDF:        {{ unit: 'mm', format: 'a4', orientation: 'portrait' }}
            }};

            html2pdf().set(opt).from(reportEl).save();
        }}
    </script>
</body>
</html>
"""

components.html(html_code, height=1200, scrolling=True)