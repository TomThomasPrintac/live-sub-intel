# תסריט צילום מעודכן — מדברים על מה שרואים

מסלול: **0 → 5 → 10 → CUT ל־65 → CUT ל־85**. קריינות באנגלית: **175 מילים**. יעד 1:50–1:55, פחות משתי דקות. [קריינות נקייה](VIDEO_NARRATION_EN.txt) · [מדריך הפקה באנגלית](VIDEO_SCRIPT.md) · [כל נקודות הזמן שנבדקו](RECORDING_CHECKPOINT_REVIEW.md).

הסרטון מתחיל במשחק עצמו. בכל קטע מצביעים על הדוגמה שמופיעה במסך. אין קטע על החלופה של מרטסאקר–פאוליסטה, אין הסבר מדובר על fallback, ואין משפט קריינות על inspection או שינוי העתיד. כללי הדיוק נשארים בהערות ההפקה.

| זמן בסרטון | מה עושים במסך | הקריינות |
|---|---|---|
| 0:00–0:10 | דקה 0, ארסנל, Balanced / Seek a win; ממשק באנגלית. מציגים את המגרש והספסל. | “Live Sub Intel helps you make the next move: who comes on, who comes off, and where everyone plays.” |
| 0:10–0:25 | מתקדמים 0 → 5 → 10. מצביעים על השעון, אירועי המשחק והסטטיסטיקות. אפשר לצלם את המעבר הראשון במהירות Fast ואז לחזור ל־Instant. | “We’re following Arsenal in a generated match, using historical player profiles and physical estimates. As time advances, events arrive and the statistics update with the game.” |
| 0:25–0:42 | CUT לדקה 65, More attacking / Seek a win; פותחים את Campbell → Oxlade-Chamberlain. מצביעים על שני השמות ועל סימון היוצא והנכנס במגרש. | “At sixty-five minutes, Arsenal are leading. The recommendation is Oxlade-Chamberlain for Campbell, adding fresh legs on the right wing.” |
| 0:42–0:59 | נשארים ב־65. מצביעים על Chamberlain בכנף ימין בהרכב המוצע, ואז פותחים Compare players & scoring ומשווים את הפרופילים. אין זום או הסבר על הזזות הקשרים. | “The proposed lineup highlights the incoming player. Open the comparison to see both profiles and the changes in attacking threat, chance creation and ball progression.” |
| 0:59–1:23 | נשארים על אותו חילוף ב־65. Broadcaster / English → Explain; בוחרים Español ומבקשים שוב. עוברים ל־Analyst ומבקשים שוב; מצביעים על נתון אחד בהסבר החילוף. | “The broadcaster explains this substitution in a short line. Switch to Spanish, and the same plan is explained in Spanish. Choose Analyst, and the explanation adds relevant match statistics and trade-offs.” |
| 1:23–1:40 | CUT ל־85, Attack / Win. מראים שארסנל בפיגור. עוברים ל־Coach, משנים Result objective ל־Avoid defeat ומראים שההמלצה משתנה. לא מקריאים סף או נוסחה. | “At eighty-five minutes, Arsenal are behind. Seeking a win calls for a tactical adjustment. Switch to avoiding defeat, and the system recommends holding the current setup.” |
| 1:40–1:55 | תצוגה רחבה ואז כרטיס סיום: שם הפרויקט, אתר, GitHub וקרדיטים. אפשר להציג על המסך חצים קצרים: match events → decision engine → Foundry explanation. | “Azure App Service hosts the match room. Microsoft Foundry selects the relevant facts and translates the explanation, so a coach and a Spanish-speaking broadcaster can follow the same decision.” |

## קישורים לצילום

- [פתיחה — 0](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=0&stance=balanced&objective=win&inspect=1&lang=en).
- [חילוף בכנף והשפות — 65](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=65&stance=attack&objective=win&inspect=1&lang=en).
- [סיום: ניצחון — 85](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=85&stance=attack&objective=win&inspect=1&lang=en).
- [השוואת מטרה — 85](https://live-sub-intel-fcfudheze9b5ewfz.swedencentral-01.azurewebsites.net/?team=1&minute=85&stance=attack&objective=draw&inspect=1&lang=en).

## לפני שמקליטים

- הממשק נשאר באנגלית; משנים רק את Explanation language ל־Español. אחרי שינוי שפה או קהל לוחצים Explain ומוודאים שהתוצאה מוכנה. כל הדגמת השפות והקהלים ב־65 נשארת על אותו חילוף של Chamberlain. מחזירים לאנגלית לפני קטע דקה 85.
- לבצע חימום לבקשות ההסבר המדויקות, ולוודא תווית מודל. לא להציג fallback כאילו זו תשובת מודל. אין צורך לדבר על כך בקריינות.
- להראות את ההרכב המוצע ואת Compare players & scoring ב־65. הסבר העמדה מתמקד ב־Chamberlain בכנף ימין; אין קטע נפרד על הזזות הקישור. להשאיר JSON ומתודולוגיה סגורים.
- ב־65 ארסנל מובילה 1–0, וב־85 היא בפיגור 2–1. ההרכב המוצע ב־65 נשאר 4-2-3-1; לא לומר שהודגם שינוי מערך או שההמלצה משנה את אירועי ההמשך.
- בכרטיס הסיום: קישורי האתר והריפו, לוגו StatsBomb הרשמי ושורת קרדיט קצרה. בתיאור הסרטון לקשר ל־DATA_SOURCES.md. [פירוט מקורות וטענות](RIGHTS_AND_CLAIMS.md).
- להקליט את הקריינות פעם אחת עם שעון. אם חורגים, לקצר הפסקות/מעברים או לוותר על נקודת דקה 10; לא להעמיס עוד הסברים. לבדוק כתוביות באנגלית ולהשאיר את הסרטון מתחת לשתי דקות.
- מסלול ההחלטות נשען על הסריקה המקומית של 228 המצבים. חיבור מודל וגרסת Azure נבדקים בנפרד לפני הצילום. עדכון התסריט אינו משנה את האתר או המנוע.
