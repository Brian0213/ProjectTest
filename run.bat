pytest -s -v -m "sanity" --html=Report/report.html testCases/ --browser chrome
rem pytest -s -v -m "regression" --html=Report/report.html testCases/ --browser chrome
rem pytest -s -v -m "sanity or regression" --html=Report/report.html testCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=Report/report.html testCases/ --browser chrome