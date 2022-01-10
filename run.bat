behave -f allure_behave.formatter:AllureFormatter -o allure-2.13.5/Results/ features/ClientScheduleSession.feature
behave -f allure_behave.formatter:AllureFormatter -o allure-2.13.5/Results/ features/CoachScheduleSession.feature
behave -f allure_behave.formatter:AllureFormatter -o allure-2.13.5/Results/ features/OpsScheduleSession.feature
allure serve allure-2.13.5/Results/