from selenium import webdriver


class SurveyGizmo():
   
        
    def start(self,acct_id, acct_email, email_receipt):
        self.driver = webdriver.Chrome()
        self.account_id = acct_id
        self.account_email = acct_email
        self.email_receipt = email_receipt

        xpath = self.driver.find_element_by_xpath
        self.driver.get('https://www.surveygizmo.com/s3/4371617/Data-Rights-Request')
        
        nxt_btn = xpath('//*[@id="sg_NextButton"]')
        nxt_btn.click()

        yes_btn = xpath('//*[@id="sgE-4371617-7-2-box"]/div/ul/li[1]/label')
        yes_btn.click()

        customer_btn = xpath('//*[@id="sgE-4371617-7-4-box"]/div/ul/li[1]/label')
        customer_btn.click()

        nxt_btn_2 = xpath('//*[@id="sg_NextButton"]')
        nxt_btn_2.click()

        acct_id = xpath('//*[@id="sgE-4371617-15-6-element"]')
        acct_id.send_keys(self.account_id)
        acct_email = xpath('//*[@id="sgE-4371617-15-8-element"]')
        acct_email.send_keys(self.account_email)
        select_delete = xpath('//*[@id="sgE-4371617-15-13-box"]/div/ul/li[4]/label')
        select_delete.click()
        email_receipt = xpath('//*[@id="sgE-4371617-15-35-element"]')
        email_receipt.send_keys(self.email_receipt)

        nxt_btn_3 = xpath('//*[@id="sg_NextButton"]')
        nxt_btn_3.click()
        print('Success!')
        self.driver.quit()

    def docs(self):
        print("""
        HOW TO USE:
            surveygizmo.start({ACCOUNT_ID} , {ACCOUNT_ADMIN_EMAIL}, {EMAIL_RECEIPT})
        """)
surveygizmo = SurveyGizmo()
