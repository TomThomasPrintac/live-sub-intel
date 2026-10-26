# מסלול צילום מומלץ — ארסנל, עד שתי דקות

נבדקו מקומית **228 מצבים**: שתי קבוצות, דקות 0–90 בקפיצות של חמש, שלוש גישות ושתי מטרות. קוד המנוע והדאטה תואמים ל־ca18fb4 שבאתר החי. זו בדיקת החלטות מקומית; לא בוצעו 228 קריאות LLM. [כל הדקות והשילובים](RECORDING_CHECKPOINT_REVIEW.md) · [CSV לפתיחה באקסל](../research/recording_route_audit_20261026.csv).

המסלול המומלץ הוא **25 → 30 → 65 → 85**. אין צורך לצלם את כל המשחק, ואת 55/60/70/75/80 אפשר להשאיר כהרחבות לשאלות. קפיצה בין נקודות מותרת, אך לא להציג חיתוך כאילו הוא ריצה רציפה.

## פעולות וקריינות

| זמן בסרטון | מה עושים במסך | קריינות באנגלית |
|---|---|---|
| 0:00–0:10 | ארסנל, 25, Balanced / Seek a win; ממשק באנגלית | “Live Substitution Intelligence turns football events into explainable bench decisions. Coaches set their intent; the system compares substitutions with tactical changes across the whole eleven.” |
| 0:10–0:24 | פותחים תוכניות ב־25. מצביעים על שני שחקני הקישור שזזים; מתקדמים ל־30 כדי להראות את השער והסימון של ראמזי | “The match is synthetic, with historical player profiles and generated physical estimates. Here, the system first recommends repositioning. Events then update the score, player markers and match statistics.” |
| 0:24–0:39 | קופצים ל־65, More attacking / Seek a win. Campbell → Oxlade-Chamberlain | “At sixty-five minutes, it recommends Oxlade-Chamberlain for Campbell. The comparison includes estimated freshness, position suitability and tactical cost, measured against the best action without a substitute.” |
| 0:39–0:54 | בוחרים חלופה שנייה, ואז שלישית: Mertesacker → Gabriel. מראים את סימון הדחייה אף שהציון 0.160 מול 0.15 | “Every alternative has its own proposed lineup. This option exceeds the numerical threshold but is still rejected: its tactical loss fails a separate quality check.” |
| 0:54–1:12 | חוזרים להמלצה הראשונה. Broadcaster / English → Explain; אחר כך Analyst. מצביעים על תווית המודל ונתון משחק רלוונטי | “Microsoft Foundry selects verified facts for the inspected plan. Broadcasters get a concise explanation; analysts get relevant statistics and trade-offs. The model cannot change the decision or its numbers.” |
| 1:12–1:22 | שפת הסבר נוספת, למשל עברית; ממשק נשאר באנגלית. מבקשים הסבר | “Explanation language is separate from the interface. Protected templates, validation and labelled fallback help preserve the selected plan and its facts.” |
| 1:22–1:40 | קופצים ל־85, Attack / Win; עוברים ל־Coach. מציגים 2–1 לליברפול ושינוי מיקום ללא חילוף; משנים מטרה ל־Avoid defeat כדי להראות Wait | “Now Arsenal is behind. Seeking a win produces a tactical adjustment; changing the objective changes the recommendation. Inspecting a plan never executes it or rewrites the match.” |
| 1:40–1:50 | חזרה לתצוגה רחבה; שם הפרויקט וקישור הדמו/הריפו בכרטיס סיום | “Azure App Service hosts the experience, with GitHub Actions testing and deploying it. Every recommendation is a proposal you can inspect, compare and question.” |

החלוקה היא יעד לעריכה. אם הקריינות ארוכה מדי, להוציא את קטע דקה 30 או את השפה הנוספת; אין לעבור שתי דקות. [טקסט הקריינות להקלטה](VIDEO_NARRATION_EN.txt).

בכרטיס הסיום של הסרטון לשמור גם לוגו StatsBomb הרשמי מהפרויקט ולצדו שורת מקור קצרה: `Historical research: StatsBomb Open Data. Physical references: SkillCorner Open Data.` בתיאור הסרטון להוסיף קישור ל־DATA_SOURCES.md בריפו. אין צורך להקריא את רשימת המקורות; הקרדיט אינו הצהרה שכל שאלות ההרשאה נפתרו. הסבר מרוכז לכל שכבות הנתונים: [RIGHTS_AND_CLAIMS.md](RIGHTS_AND_CLAIMS.md).

## קישורים מוכנים

- [פתיחה — 25, מאוזן / ניצחון](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=25&stance=balanced&objective=win&inspect=1&lang=en).
- [שער — 30, מאוזן / ניצחון](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=30&stance=balanced&objective=win&inspect=1&lang=en).
- [הדוגמה המרכזית — 65, התקפי / ניצחון](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=65&stance=attack&objective=win&inspect=1&lang=en).
- [סיום — 85, התקפי / ניצחון](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=85&stance=attack&objective=win&inspect=1&lang=en).
- [השוואת מטרה — 85, התקפי / תיקו](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=85&stance=attack&objective=draw&inspect=1&lang=en).

## דיוקים שחשוב לשמור

- ב־25 זו החלפת צדדים בין Flamini ל־Ramsey באותה צורה, **לא שינוי מערך**. כל ההמלצות שנבחרו לארסנל בסריקה נשארות ב־4-2-3-1. אין לומר בסרטון שהודגם מערך חדש בארסנל.
- ב־65 Campbell כבר עם צהוב, אבל אין לטעון שהכרטיס הוא רכיב עצמאי שמפעיל את ציון ההמלצה. הצהוב מופיע בהקשר ובהסברים; ההמלצה מושפעת בעיקר מרענון ומאילוצי האיכות במצב הזה.
- ב־85 / Win תועלת שינוי המיקום היא 0.21695; החלופה עם חילוף מוסיפה רק 0.11498 מול המהלך הטוב ביותר ללא חילוף. ב־Draw החלופה הטובה מקבלת 0.14756, מתחת ל־0.15. ההמתנה אינה הוכחה שזו החלטת מאמן נכונה; זה גבול מדיניות שקוף שאפשר לבחון.
- בתרחיש יש חילופים מתוסרטים, כולל Campbell → Oxlade-Chamberlain ב־74. הם אינם ביצוע של לחיצת Inspect ולא אימות בלתי תלוי של איכות ההמלצה.
- לפני צילום: חימום לבקשות ההסבר שיופיעו, בדיקת תווית המודל והגרסה. אם מופיע fallback, לא להציג אותו כקריאת מודל מוצלחת. קריאה מה־cache מסומנת ככזו ואינה בעיה אם מתארים אותה נכון.
- להקליט מהאתר החי. ה־PR מסיר מהממשק את הודעת אי־השיוך שנוספה כאמצעי זהירות. תיעוד המקורות המדויק נשאר במסמכים; לוגו וקרדיט StatsBomb והקישור למקורות נשארים בתחתית. השינוי דורש מיזוג ופריסה לפני שיופיע ב־Azure.
