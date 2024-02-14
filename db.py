from sqlmodel import create_engine, Session, SQLModel, select
from models.org_model import Organization, Financials, Tag

database_url = "sqlite:///./db.sqlite"
engine = create_engine(database_url)


def create_db():
    try:
        SQLModel.metadata.create_all(engine)
    except Exception as e:
        raise e


def insert(data: Organization):
    with Session(engine) as session:
        query = select(Organization).where(Organization.inn == data.inn)
        existing_organization = session.exec(query).first()

        if existing_organization:
            print(
                f"Organization already exists in the database, skipping insertion: {existing_organization}"
            )
            pass
            # TODO: update the existing organization with new financial data if it is present
        else:
            session.add(data)
            session.commit()
            session.refresh(data)
            session.close()


def get_or_create_tag(tag_name: str):
    with Session(engine) as session:
        query = select(Tag).where(Tag.name == tag_name)
        existing_tag = session.exec(query).first()

        if existing_tag:
            print(
                f"Found tag: {tag_name}, will use {existing_tag.name, existing_tag.id}"
            )
            return existing_tag
        else:
            new_tag = Tag(name=tag_name)
            print(
                f"Not found tag: {tag_name}, will created new {new_tag.name, new_tag.id}"
            )
            return new_tag


def get_org_financials(inn: int):
    with Session(engine) as session:
        statement = (
            select(Organization, Financials)
            .join(Financials)
            .where(Financials.inn == inn)
        )
        query = session.exec(statement).first()
    return query if query else None


create_db()
