import requests
from bs4 import BeautifulSoup
from sqlite3 import connect

db = connect("papers.db")
cursor = db.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS papers (
        guid TEXT PRIMARY KEY,
        title TEXT,
        link TEXT,
        abstract TEXT,
        pubTime TEXT
    );
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE
    );
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS paper_categories (
        id INTEGER PRIMARY KEY,
        guid TEXT,
        category_id INTEGER,
        FOREIGN KEY (guid) REFERENCES papers(guid),
        FOREIGN KEY (category_id) REFERENCES categories(id)
    );
    """
)
db.commit()


arxiv = "https://rss.arxiv.org/rss"
categories = {
    "ai": "cs.AI",
    "cv": "cs.CV",
    "nlp": "cs.CL",
    "ml": "cs.LG",
    "robotics": "cs.RO",
    "graphics": "cs.GR",
    "retrieval": "cs.IR",
}


def get_papers(url):
    """
    Fetches the latest papers from the given URL and returns a list of dictionaries containing paper details.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="xml")

    papers = []
    for item in soup.find_all("item"):
        title = item.title.text
        link = item.link.text
        abstract = (
            item.description.text.split("Abstract: ")[1]
            if "Abstract: " in item.description.text
            else item.description.text
        )
        guid = item.guid.text
        if guid.startswith("http"):
            guid = guid.split("/")[-1]
        else:
            guid = guid.split(":")[-1]
        guid = guid.split("v")[0]
        time = item.pubDate.text  # estern time

        papers.append(
            {
                "title": title,
                "link": link,
                "abstract": abstract,
                "guid": guid,
                "time": time,
            }
        )
    return papers


for category, code in categories.items():
    cursor.execute(
        """
        INSERT OR IGNORE INTO categories (name)
        VALUES (?)
        """,
        (category,),
    )
    db.commit()
    cursor.execute(
        """
        SELECT id FROM categories WHERE name = ?
        """,
        (category,),
    )
    category_id = cursor.fetchone()[0]
    print(f"Fetching papers for category: {category}")
    url = f"{arxiv}/{code}"
    papers = get_papers(url)
    for paper in papers:
        cursor.execute(
            """
            INSERT OR IGNORE INTO papers (guid, title, link, abstract, pubTime)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                paper["guid"],
                paper["title"],
                paper["link"],
                paper["abstract"],
                paper["time"],
            ),
        )
        cursor.execute(
            """
            INSERT OR IGNORE INTO paper_categories (guid, category_id)
            VALUES (?, ?)
            """,
            (paper["guid"], category_id),
        )
    db.commit()
