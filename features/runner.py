import subprocess
if __name__ == '__main__':
#command line args along with error capture on failure with check true
# running program with allure
      try:
            s = subprocess.run('behave -f allure_behave.formatter:AllureFormatter -o Reports --no-capture',shell=True, check=True)
      except:
            pass

      r = subprocess.run('allure serve Reports',shell=True, check=True)


#running feature by excluding file

      # Exclude = subprocess.run('behave --exclude ScheduleSessionGmail.feature --no--capture',shell=True, check=True)