"""Analysis persistence and AI orchestration."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from gemma import analyze_with_gemma
from models import Analysis
from schemas import AnalysisCreate


def create_analysis(db: Session, request: AnalysisCreate) -> Analysis:
    findings, recommendations = analyze_with_gemma(request.input_text)
    analysis = Analysis(
        input_text=request.input_text,
        findings=findings,
        recommendations=recommendations,
    )
    db.add(analysis)
    db.commit()
    db.refresh(analysis)
    return analysis


def list_analyses(db: Session) -> list[Analysis]:
    return list(
        db.scalars(select(Analysis).order_by(Analysis.created_at.desc())).all()
    )
