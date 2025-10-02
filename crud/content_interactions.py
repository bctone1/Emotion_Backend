from sqlalchemy.orm import Session
from models.content_interactions import ContentInteraction

def create_content(
        db: Session,
        session_id: str,
        recommended_emotion: str,
        content_type: str,
        content_title: str,
        viewing_completed: bool,
        stopped_early: bool,
):
    new_content_data = ContentInteraction(
        session_id=session_id,
        recommended_emotion=recommended_emotion,
        content_type=content_type,
        content_title=content_title,
        viewing_completed=viewing_completed,
        stopped_early=stopped_early,
    )
    db.add(new_content_data)
    db.commit()
    db.refresh(new_content_data)
    return new_content_data
