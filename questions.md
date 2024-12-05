
```

Q: How is the frequency of callback for the webhook? Do you have a job for each payroll, right? How frequently do you collect data from the payroll system?
A: We run the Linked Accounts checks weekly.

Q: If a user leaves the job, how long will this data be reflected to our webhook?
A: That depends on the timing between when the payroll system is updated and when the next job is run to check the state of the system. if they leave on monday and we check on tuesday, then the webhook is sent on tues. if we run the job on monday and they leave on tues, then we wouldn’t know until the next monday.

Q: Imagine a user was fired on day 14. The next syncs would happen only on 16, 23, 30. Could the HR update that this user was fired on the last day and we would only know about in the  next month? I will send a image for context later.
A: Same as above. the next time the job is run after the employee was fired and the payroll system was updated, we would see this reflected in the data.

Q: How much time usually we have for having a linked-account-disconnected ? How much is the expiration of a connection with Atomic?
A: We maintain the connection until it doesnt work anymore, the user's credentials are no longer valid (e.g., password change), our customers contract expires, or the user asks that we remove their data.

Q: If the user was fired on Jan 22th when are we going to be notified by this in the webhook?
A: The next time the job is run to check for any differences in the payroll system.

Q: What is the frequency of the job run?
A: This is run weekly.

Q: Can we force the sync everyday with Linked Account sync? Can we force more than one time per day?
A: Yes, at this time, you can. We are investigating putting limits on API traffic, but will let you know if we decide to do that.

Q: If we have to send a million requests per day to keep in sync our users, can your services be healthy?
A: We have yet to run into problems with the traffic from any of our customers, but we are actively looking at rate limiting requests. Our system is built on Lambda and Kubernetes, so it can handle   quite a bit of load. That being said, if you are planning on polling the payroll systems through Atomic, security measures on the payroll side may be triggered so we would prefer you not do that.

Q: How do you guys link our user identifier to yours user _id? During the login? 
A: During the access-token creation. We create an _id for the user with the details sent at that point.

Q: Can we regenerate a new token for this user without forcing the login?
A: We prefer that the access-token be created each time a user enters the flow (it has a 24 hour lifespan). What are you trying to do here? Unless the users credentials are stored via a Linked Account, the user must authenticate through the payroll system. Why do you need to create a different token for the user?

Q: what if our services is down can we have a way to sync lost requests?
A: yes, we have the ability to replay webhooks, if needed. Its a manual process at this time, but can be done
```

```

Q: Is there a Webhook event available to track the PayLink journey, such as how many users opened, submitted, and completed the task, similar to what you have on the [console](https://console.atomicfi.com/)?
A: No, you'd need to listen for UI events to capture the user behavior data. Webhooks only trigger on Task level events.
```

```

Q: If a debit card is used to switch the card on file, will we receive this as a debit card or a checking account in the webhook? I assume it would be a debit card, but please confirm.
A: it would be a debit card
```

```

Q: What is an automated direct deposit switch? 
A: Direct deposit switching enables customers to update their direct deposit inside of the banking app or online banking. 

Q: How does it work?
A: Atomic works by allowing the customer to securely authenticate directly into their payroll provider inside the banking app to switch their direct deposit. 

Q: Why are we offering automated direct deposit switch to our customers? 
A: Allowing customers to easily switch their direct deposit helps them fund their account with their paycheck, enhances the user experiences and improves their loyalty. 

Q: What are the most common error codes for deposit switch?
A: Bad-credentials: The end user inputs incorrect credentials for connecting to the payroll system. Product-not-supported: The payroll system doesn’t allow the end user to update their direct deposit. This can happen due to either payroll or employer configurations removing that capability from the end users.  Account-setup-incomplete: The user has not fully set up their online account with the payroll system.  User-abandon: The user exits the flow when more details are required. MFA is the main reason for this.

Q: How long will it take for my direct deposit setup to take effect? 
A: It can take 1 to 2 pay periods for the change to take effect. However, this can vary by employer or payroll provider.

Q: What if I don't see my employer?
A: There are over 2.1 million employers supporting ~85% of the U.S. workforce. If you can’t find your employer or payroll provider, we provide a prefilled PDF with the information you will need to set up direct deposit with your employer or payroll provider.

Q: What if I don't remember my employer or payroll login? 
A: Most employers or payroll providers allow you to recover your login credentials as you are setting up your direct deposit through the banking app. However, depending on your employer, you may be required to complete the recovery process outside of the DIY direct deposit setup and then come back to the banking app to complete the setup. 

Q: How will I know if my direct deposit switch was made successfully?
A: You will get a confirmation email from the bank if the direct deposit setup was successful. You can also log in directly to your employer or payroll provider and verify the update.

Q: How can I update my direct deposit for social security or other federal benefits? 
A: Online: For Social Security benefits, use the bank's paper direct deposit method. For other federal benefits, visit godirect.gov. Phone: Call the Social Security National 800 Number at 800-772-1213. In person: Visit your local  SSA office.

Q: How does it work? Why does Atomic ask me to enter my payroll information?
A: With Atomic you can easily update your direct deposit information inside your bank's mobile or online app. You will find your payroll provider, enter in your credentials, select which bank account you want your paycheck to be deposited into, and confirm the transaction. Within 1 to 2 pay cycles your paycheck will be automatically direct deposited into the new account. 

Q: How many payroll providers does Atomic cover?
A: Over 450 unique integrations to large payroll providers (ADP, Paychex), corporate employers (Walmart, Amazon), government systems (Unemployment, DFAS- Armed Forces), and gig platforms (DoorDash, Uber).

Q: Is entering my information in the Atomic SDK feature secure?
A: Please refer to the Atomic Data Security policy. 

Q: What if I don’t know my credentials?
A: If you do not know your payroll credentials, you may go directly to your payroll providers website and follow their reset or setup instructions. If you do not know your payroll provider or do not have an online user account, you will need to contact your company's HR department for assistance.

Q: How many attempts do I have before my account gets locked?
A: Since you are logging in directly to your payroll provider, the account locking criteria is determined by them and not by Atomic. If you need to reset your password or unlock your account please contact the payroll company directly. 

Q: What if I do not want to enter my credentials?
A: If you do not wish to enter in your credentials you may select the manual option that will generate a PDF document you can give to your Human Resources department. 

Q: How can I revert a direct deposit switch?
A: To revert your direct deposit, log in to your employer's payroll system and manually update your bank account to the desired account. If you need assistance, please contact your HR department. 

Q: Are there minimum or maximum amounts for a direct deposit switch?
A: No.

Q: Will existing allocations be overwritten when I complete a full switch?
A: If the request for a deposit allocation is compatible with the accounts currently on file and overwriting is allowed by the payroll system and employer in question, then yes, an existing allocation can be overwritten.
```

```

Q: Where do I find Atomic’s API docs?
A: https://docs.atomicfi.com/

Q: What is Transact? What does Atomic’s Direct Deposit product look like?
A: Please see this video for an overview of Atomic’s Transact including a happy path walk through. https://www.loom.com/share/cb4dc50e5da04e99b2f61ee02d55f272?sid=056be1c3-beae-4600-ae47-7d8b73750f89

Q: How do I log into Console?
A: You should receive an email with an invitation to login into the Console. Please note this link expires after 24 hours so you’ll need to register within that time frame. Link: console.atomicfi.com 

Q: I forgot my Console password - how can I reset it?
A: Use the “Forgot password?” prompt to reset your password.

Q: I’m having trouble getting into my account- who can help me access my account?
A: Admin’s are able to delete users and re-add users who are unable to log in. Contact your account admin to assist.  If further assistance is needed, please contact us at cs@atomicfi.com.

Q: How can I see tasks?
A: Tasks are found on the “Tasks” tab in console.  View all by scrolling down the page or click on a specific task to bring up details.  When a single task is selected it will show: Status, Fail Reason(if any), Action, Amount, Routing Number and the last four digits of the Account Number. You are also able to see the webhook events for the task.

Q: How do I navigate to specific tasks in console?
A: Customers can search in Console by - • Task ID: 6335f7220bf8f900096457f0 • User ID: ex:email address Alternatively filter tasks by status: Queued, Processing, Completed or Failed.

Q: Why does the task say “failed”?
A: For Atomic’s deposit product, when a task says “failed” Atomic was unable to switch direct deposit for this user.  For Atomic’s verify product, when a task says “failed” Atomic was unable to collect the required information for this user.

Q: What does this fail reason mean?
A: In addition to the descriptions in the API docs, below is additional information about task fail reasons that could be encountered. @End User Support Guide 

Q: Will the end user know why the task failed?
A: Ending states can be found here in the Figma section of the Atomic Knowledge base.

Q: Can I export the task data?
A: At this time, task data can not be exported from Console.  Please contact us at cs@atomicfi.com for data requests.

Q: How do I navigate through the Emulator?
A: The back button labeled “Transact SDK” will allow you to go back to a menu selection screen. From there you can navigate as needed through the flow.

Q: Is there a way I can demo the Atomic product to others?
A: Yes. Within the Emulator Tab of Console, there is a demo option. Navigate to Emulator → Transact SDK→ Demo. Here you can add the name and logo you’d like to appear in the UI. This can be used to show others the Atomic experience.

Q: What customizations can be made to the SDK?
A: Several customizations can be made to the SDK, including, but not limited to: • Under “Theme” - see “Styles” and “Fonts”. Styles allows you to select color branding which will reflect in some of the buttons, as well as adjust your button border radius. For Fonts, we have a number of Google fonts available to choose from. • Under “Initialization” - Customize whether a user journey begins on the consent, search, or login screen. Can also choose between English or Spanish. Can select Deposit, Verify or both products and are able to choose the order in which they occur. • You are able to toggle between Light Mode and Dark Mode with the drop down in the upper lefthand corner. **When customizing verbiage be sure to select “Review Customizations” and then “Publish to Production”.

Q: Can you skip screens within the Atomic flow?
A: You can skip the Intro screen, or create your own. You can also Deeplink past the Search Screen directly into the payroll provider/employer login page if this information was passed on from another source. This can be done under the Initialization tab in the Transact SDK. You are able to skip our failure/success screen if you’d like to build your own.

Q: What front end events are emitted in Transact?
A: Emitted events can be seen in the “Events” panel on the right-hand side in Emulator.  Events will auto populate after initializing Transact. Learn more about events in the Guides section of our API docs.

Q: What is the Deposit Scenario Simulator?
A: The Deposit Scenario Simulator allows you to test out different end user scenarios and discover where the money will go based on the given inputs. For example: a user setting up their direct deposit for the first time, or a user setting up a fractional amount with two other accounts already on file.

Q: What is Figma?
A: Figma is a collaborative browser-based interface design tool that Atomic uses to create digital prototypes. You can see our designs in Console by navigating to Resources → Figma

Q: Where can I find flows to plan and build?
A: On the “Resources” tab in Console, several flows are illustrated.  The Deposit Flow, Verify Flow, Search, Fractional Deposit, Authentication, Ending States and more!

Q: What does the user see when their task is successful?
A: Success Screen Image. You can see this in our Figma designs, or by using test-good when going through the Emulator.

Q: What does the user see when their task fails?
A: There are several screens a user can see when their task fails.  Please see the Figma page called “ending states” for more details.

Q: How can I change roles/permissions of a user in Console?
A: Only Admin, Production Developer, and Sandbox Developer users can edit user roles and they can only edit roles for users whose role is equal to or less than their role (e.g. a Sandbox Developer cannot edit the role of a Production Developer). This is done on the Settings →Team page by clicking the action menu on the right side of the user's card. To view which permissions are attached to each role, use the tab Roles & Permissions on the left hand menu bar. Please see the video below for how to change Console roles and permissions.

Q: Can I have multiple secrets?
A: Yes, to facilitate multiple testing environments, multiple secrets can be created.

Q: How many secrets can we have?
A: You are able to create an unlimited number of secrets.

Q: Which settings or features can be turned on and/or off?
A: Under Settings > Features there are several self-serve features that can be enabled or disabled, including: • Manual Fallback Call to Action - Enabling this will present a button on the Zero Search Results for Payroll screen and Authentication Error screen. This will allow you to have users fallback into a manual option within your app/website. You will receive Webhook notifications on these events. • Fractional Deposits -  Fractional Deposits allows your users to customize their deposit distribution in Transact.  Some users may not be ready to move their entire direct deposit over to their newly created bank account. In order to overcome this, we recommend allowing users to build trust by enabling fractional deposits.  Where available, this will allow users to choose between a fixed amount, or a percentage(%) of their deposit when configuring their new distribution. A “Primary Distribution type” can be selected through the drop down menu. This will show up as the default suggestion when a user first encounters this screen. This feature can be enabled in the Features section of your Atomic Console.  Please also see: https://docs.atomicfi.com/products/deposit/best-practices • Manual Instructions -  Not every employer allows the user to instantly switch their direct deposit. In these cases, we have a full time team dedicated to providing precise step-by-step instructions for these users. Manual Instructions allows your users to view instructions to switch their direct deposit which may include calling a phone number, filling out a specific form, or visiting a website after logging into their employer-issued VPN. An example of this is the employer, Starbucks. We recommend enabling this feature on your account to benefit from our research.  Please also see: https://docs.atomicfi.com/products/deposit/best-practices Please note in these cases, Atomic is unable to track the status of manual direct deposit switches. • Bounded Fractional Deposit - This allows you to set an upper and lower limit on the fractional deposits. These can be hard or soft limits. To set a hard limit you must select the check box “Enforced” next to the limit. You can also go into the Emulator to customize you warning/limit message verbiage. At this time, bounded fractional deposits can only be done in fixed amounts, not percentages(%). 

Q: How do I move from Sandbox to Production?
A: This can be done within Emulator. There is a dropdown button at the top right hand corner that allows you to move between Sandbox and Production.

Q: Is there a way to test Webhooks?
A: Webhooks can be tested in Console under Settings > Webhooks.

Q: Can I test events being emitted?
A: Test events can be emitted in Console under Settings > Webhooks.  Choose your event, secret, product and distribution to get the exact scenario you’re planning for!

Q: I think I’m having firewall issues.  What can I do? Are there certain IP addresses I can Whitelist?
A: Traditional Financial Institutions and those with a VPN will need to Whitelist the following IP addresses: wss://ws-mt1.pusher.com/ ingest.atomicfi.com cdn-public.atomicfi.com atomicfi-public-sandbox.s3.amazonaws.com atomicfi-public-production.s3.amazonaws.com ws-mt1.pusher.com api.atomicfi.com sandbox-api.atomicfi.com cdn.atomicfi.com cdn-sandbox.atomicfi.com atomicfi.com transact-sandbox.atomicfi.com transact.atomicfi.com

Q: Who do I speak to about billing?
A: If there are questions about your bill, please contact us at AP@atomicfi.com. Perhaps you did not receive a bill, the bill was not as expected, a new billing address needs to be added to the system or further discussion is needed.

Q: Do you see your fair share of ID theft, fraud or bad actors?
A: Going to the payroll system yourself with concerns is the best for discussing ID theft.  Atomic has not seen this very often.

Q: Will we be able to tell if the username or password was incorrect?
A: No we do not have that level of granularity - only that  the combination was incorrect.

Q: Why do you show it will take 1-2 pay cycles for the direct deposit switch to take effect?
A: This varies system to system and also employer by employer.  Some have a manual approval process for Direct Deposit switch.  Actually seeing the deposit hit the account is something Atomic does not play a part in.  Atomic only writes the change into the system.  We estimate it to take 1-2 pay cycles for the change to take effect.

Q: What is the “Linked Accounts” feature?
A: Enabling this will save a user's credentials upon successful authentication for reuse later without the user present.

Q: What is the “Uplink Automation” feature?
A: Allows users to run tasks on the domain of their device instead of the Atomic cloud. Please also see: https://atomic.financial/insights/introducing-uplink/

Q: What is the “Manual Upload of Employment Documents” feature?
A: With Atomic’s Verify product, enabling this will present a button on the Authentication Error screen. This button will allow a user to upload their paystubs manually in attempts to run the verify product.

Q: What is the “Account Swapping Detection” feature?
A: Restrict individuals from re-using credentials on different user accounts.  Please contact us at cs@atomicfi.com for more information.

Q: What is the “Verify” product?
A: If utilizing Atomic’s Verify product, desired fields are available to self-serve in the features section of Console. We recommend customizing the data fields you’ll be needing to return via the Features section of your Atomic Console. Given your use case, you can determine which data fields will be required to achieve your end result. Please also see: https://docs.atomicfi.com/products/verify/data-scoping Principle of least privilege In order to protect your users and optimize your experience, a best practice is to only retrieve the data that is needed. In addition to added protection, there are cases where your field selection can impact the user experience. An example of this is retrieving not only the W2 wages as structured data, but also opting into retrieving the associated PDF form. By enabling the retrieval of the form, the user is may be prompted to go through a 2FA experience during their authentication process in order to secure the transaction. Although this is not likely to impact your conversion rate, it could present friction in the case where you’re planning on implementing our Linked Accounts feature to periodically update the user’s income data without needing their presence in your application.
```

```

Q: on the call Friday, Atomic mentioned that you all had been working on some paystub updates with Paylocity and UKG (?) and that we'd get some more updates on Monday. Are you ready to share the list of what's upcoming? Thanks!
A: yes we recently added support to source data from the statement PDFs for those two. It can be available in a parsedData object on the statement and the data can be merged into the base data (and marked as such) when the standard integration can’t provide it
```

```

Q: What is the Atomic SDK?
A: The Atomic SDK is a lightweight wrapper around an iframe or WebView. The parameters passed into the SDK are used to drive functionality within the UI of the iframe.

Q: Do I need to use the SDK? 
A: A native mobile SDK is required to run TrueAuth, which is required for PayLink flows and has a significant positive effect on UserLink conversion where available. Utilizing the SDK is highly recommended if a native app is available. The other significant advantage of TrueAuth, and the reason we built it, is that credentials need not be transferred to any third-party, including Atomic. The users device interacts with the third-party system directly, rather than Atomic becoming an intermediary between the two. For browser or Javascript environments, you can either use the JS SDK, embed the SDK via a <script> tag using UNPKG or a related service, or build the Transact /initialize URL yourself and launch directly into the iframe. This will eliminate you from using the callbacks made available via the SDKs however, so you will not be able to use the onClose events to close the iframe or to take advantage of our manual fallback flows.

Q: Can I just use your APIs?
A: While a significant portion of our product is available via API, we do require that our Terms and Conditions are displayed to the end user. Our legal framework for accessing the systems we access on behalf of the user require their authorization.  Additionally, there is quite a bit of nuance across all of the connected systems we integrate with which is handled by Transact out of the box. It would be a significant development burden to recreate all of the functionality we offer from a single instantiation point.

Q: How big is the SDK and what sort of impact with this have on my deployed bundle size?
A: - iOS: 1 mB    - Javascript: 2.2kB minified, 1kB gzipped - Android: 0.3 mB

Q: What is your SDK upgrade cadence?
A: We release bug fixes every couple of weeks, with minor updates happening about once a year. Because the SDKs are thin wrapper around WebViews, we are able to publish internal updates to Transact without needing to ship updates to the SDKs themselves. We maintain rigorous backwards compatibility and only update the SDKs when surface of the SDK needs to be modified. This does not happen all that often, so the maintenance burden is pretty light.

Q: How does the SDK authenticate with Atomic backend?
A: A publicToken is required to be present in order to initialize Transact. This publicToken is created by hitting the /access-token endpoint in the Atomic API from your services layer and then embedded into the headers of all communications between Transact and the Atomic API. This API call to create the publicToken is also the means by which sensitive data required to complete a flow within Transact is transmitted to Atomic so that any sensitive data does not need to go through the client side application. The call to /access-token is secured via API keys and secrets exchanged via the Atomic Console.  

Q: How does Atomic manage sessions? 
A: Non-persistent. We do not maintain client-side sessions 

Q: What type of device/customer data is being collected by the SDK?
A: We collect a few pieces of device data in order to drive product development and troubleshoot issue which may be caused by device specific nuances.     "$browser"     "$browser_version"     "$device"     "$device_id"     "$os": "iOS",     "$screen_height": 812,     "$screen_width": 375,

Q: How secure is the connection between the client devices and Atomic API? Is traffic encrypted?
A: Yes, all traffic from Transact is sent via secure network protocols; either HTTPS or WSS connections. 

Q: Why does TrueAuth require a native SDK?
A: TrueAuth runs by spinning up an additional WebView in a background process which is orchestrated by the main Transact process. The background process is used to direct the user to the domain in question so they can authenticate into that service without sharing the credentials with Atomic. We then use the session created in the background process to fulfill the requested operation. This type of functionality is not supported in any browser but is in the mobile platforms.

Q: How does the WebView work?
A: We use the native WKWebView on iOS and webkit.WebView on Android to connect to predefined URLs for the service providers.  Using postMessage() calls on iOS and @JavascriptInterface decorators on Android, Atomic has strictly defined message passing built out where predetermined events pass expected events from the WebView to the SDK. This drives required functionality where needed, but due to the defined nature of the flows, disallows any arbitrary code execution. The WebViews do not use any sessions and local storage is only used to temporarily store metadata for the app to function; no user data is ever put into device storage.

Q: Is arbitrary code execution prevented? Can code be executed bi-directionally?
A: Yes arbitrary code execution is prevented and code cannot be executed bi-directionally.  The iOS SDK uses postMessage() calls which pass messages to the SDK via a WKScriptMessageHandlerWithReply protocol. These are handled with the userContentController to sanitize events and route them to the relevant predefined flows within the app. Similar message passing flows are used to control the code flow in the Android SDK. This eliminates the possibility of arbitrary code execution.

Q: What are Atomic’s software security processes? 
A: All code is reviewed through peer review as well as automated and authenticated scanning tools before release to production to identify coding flaws and security concerns, including inappropriate storage of secrets. All identified critical and high coding flaws and security concerns must be remediated before the push to production and after any material upgrades or modifications. Code is independently reviewed by multiple engineers and tested before release to the production environment. Our SOC controls define required approvals for security and application changes. We use Dependabot (for SCA testing), npm-audit, and Amazon ECR scanning to identify package and dependency vulnerabilities. We manually run SAST scans with semgrep on an ad hoc basis and capture findings in our issue tracking system. We use ESLint, a static code analysis tool for identifying problematic patterns found in code. Automated DAST scanning is performed weekly with OWASP Zed Attack Proxy. Atomic applies additional controls relating to resource access, logging, and monitoring using Datadog, StrongDM, JumpCloud, AWS CloudWatch, CloudTrail, and GuardDuty.

Q: Are there measures in place to prevent or control JS vulnerabilities, such as Cross-Site Scripting (XSS) attacks?
A: See above but we also have rigorous testing for both DAST and SAST, as well as review and branch protection policies on our code repositories.

Q: How does the SDK handle the transmission of sensitive data within the WebView?
A: Via postMessage calls or strictly defined events as documented above. If sent to the Atomic backend it is sent via HTTPS calls to our API.

```

```

Q: Have any of your clients used User Session IDs as a unique identifier?
A: No - we discourage this since it breaks the ability to link multiple sessions from the same user together. More difficult for support, could break product enhancements (such as the return user experience), and cloaks fraudulent behaviors from users that span multiple sessions.
```

```
Q: I have a question about webhooks .. I assume that Atomic will be sending only events specific to Capital one customers to the Webhook api endpoint . Is that assumption right ? How does Atomic filter CapitalOne customers?
A: That is correct. We use the API key to segregate the traffic internally so we'll only send webhooks for Tasks associated with the API key in the associated Atomic env (sandbox|prod)
```

```
Q: Does your system have the ability to connect to any international payroll providers?
A: At the moment, we’re only operating within the U.S., but we’re actively exploring opportunities to expand into other countries.
```

```
Q: We've processed the W2 test data you've sent us, but are hitting some errors with invalid input. I can see that in one of the jobs returned for the user with the `example-good@` email, with issuer "Acme Inc.", there are two locality entries where the localTaxWithheld is greater than the localIncome: In locality "One", the income amount is 24.56 but the tax withheld is 78.56, and in locality "Two" the income amount is 45.45 but the tax withheld is 65.48. Since you cannot withhold more than you earned when e-filing, these values need to be altered.
A: This is just sample data to facilitate building integrations with our system. The values within the data are not overly relevant and do not come from a payroll source. 

```

```
Q: Are there plans to support french language at all? 
A: At the moment, we don’t support it, but we’ve had internal discussions about potentially supporting French in the future.
```

```
Q: hi Atomic team, we want to check with you currently is there’s any upper limit on the direct deposit amount that user can key in from this screen ?
A: No, I don't believe there is. However, you can set an upper limit within your "Features" tab to prevent users from proceeding above a certain amount. This limit can be a hard or soft limit, depending on whether you click the "Enforced" button.
```

```
Q: General question that came up during an internal discussion -- when the borrower uses a credential-less flow through the Atomic widget, is the borrower's password reset with the payroll provider?
A: No. it shouldn’t. ADP just has a second flow that users can access when they don’t know their username and password.
```

```
Q: We need to update our third party details, and one of the questions is if you use cloud storage, and if it’s private our public.
A: MongoDB is hosted on AWS. All data is stored in and accessed from the US. We don't have our own private cloud. We use third party providers (public cloud).
```

```
Q: What the type of failures we could expect to see in bill switch aside from bad user credentials.   Do we have list of fail types for Switch?
A: Tasks may fail for many different reasons. If a Task fails, we will include a reason property with the event's data object. Possible values include: subscription-inactive The subscription selected is currently inactive. subscription-managed-by-partner-provider The subscription selected is managed by a partner provider. The payment method will need to be updated via the partner provider's portal. payment-method-locked The payment method selected is currently locked in the service provider's system. The user will need to try again after the lockout has ended. payment-method-not-supported The payment method selected is not available to be used in for the select service provider. Another payment method will need to be used. payment-switch-unsuccessful The payment switch was unsuccessful. We are uncertain as to the nature of the failure reason, but are unable to switch this user's payment method with this service provider at this time.
```

```

Q: Can you please help me to understand exact flow of long tail merchant here . Does card environment has api which make a request to Merchant ? Or its API who requests merchant by pulling card data from card environment.  Also I see the device call to merchant only for authentication , does that mean even for  non long tail merchant , device go to api to make a switch ?
A: Yes the card data is hosted in a completely separate environment. With some long tail merchants, we may have an API request to update card data on the merchant. This request proxies through the CDE. Inside of the CDE, card data is added to the request before it is sent outbound to the merchant (push not pull). This diagram only illustrates the long tail approach. In the TrueAuth approach, the device detokenizes directly with the CDE and an API request that includes the card data is then sent from the device itself to the merchant.

Q: Can you please elaborate point 2 what do we mean by proxy and push? I am trying to understand how does it work.  is it like Atomic API make a call to another API hosted on CDE environment which will pull data from database on CDE and then sends call to merchant ?
A: Yes - your description makes sense. Atomic environment sends the shape of merchant request to the CDE CDE detokenizes and forwards the request to the merchant.  On the CDE we use what Basis Theory calls a “Ephemeral Proxies”. 

Q: Circling back to the actual questions all these started with: Is this process also followed for non long tail merchants? if not, how does the API call shown in Ephemeral Proxies help with long tail merchants. you explained earlier that long tail merchants don’t have an API available, hence the need to be performing the switch via headless cloud devices
A: Even if the merchant does not have an API, for example, it may be a form POST request, we make sure that request gets proxied through basis theory where we submit the form with example card data intentionally, and then the proxy swaps it with the real card data before it actually goes out to the merchant.

Q: For a non long tail merchant (those that have an API to add card on file), does the switch request ever initiate from the CDE?
A: The following merchants use ephemeral proxies: disney espn grubhub hulu max paramount plus There isn’t any particular reason they use proxies - they could use either, except that that were built early in the product lifecycle and we were validating this approach. So, as it stands, the answer is “Yes”. Apologies for the delay - I had to have an engineer go dig through the code and find out which ones use the proxy. For a merchant that supports API, the above list shows which ones are through the Ephemeral Proxy (CDE).

Q: For other merchants that are not in the list but have an API (eg: Netflix), it never goes through the Ephemeral Proxy (CDE). The SDK pulls card data from CDE CDE decrypts and sends them to SDK SDK calls Merchant API from SDK
A: Yes

Q: but even if we see high traffic at a merchant that doesn't have an API to store card data we would still need to use the CDE, right?  my understanding was it has less to do with traffic and more to do with how the merchant website works
A: We can handle those types of connections through the device too, but the integration is cost-intensive from an engineering perspective. It wouldn’t make sense to use this approach for the thousands of bespoke utility systems with low volume per integration. Others, like LADWP, even if there isn’t an API, we’d likely roll it out via TrueAuth anyways. It has more to do with traffic, but is a a combination between traffic + API availability.

Q: does this mean that SmartAuth is synonymous with those merchants who we could support device connections with?
A: SmartAuth is from our backend -> merchant (primarily used on longtail connections) TrueAuth is from the device -> merchant

Q: A couple more questions: If we wanted to request that a merchant without an API does a client-to-client switch, what would the process of making that change look like? What does the process look like if we wanted to request a SmartSwitch merchant  become TrueAuth?
A: These two questions look the same to me. Both describe moving an integration from processing in our backend to processing on the client (TrueAuth), right?

Q: Perhaps I'm a bit confused. Based on the conversation above, it seems like authentication (TrueAuth vs SmartSwitch) can be decoupled from the method in which we store information at a merchant. For example, as mentioned previously in the thread, Disney+ and Max are both TrueAuth that use the CDE env to store credentials on file. What I'm trying to get is the answer to If we wanted to onboard an existing SmartSwitch merchant to TrueAuth (i.e. Chipotle) what inputs would be needed from us (the client)? How many TrueAuth client-side only merchants can you support at a given time? Moving forward, are we coupling TrueAuth merchants with client-side only processing? Does the process look different for a net new merchant we'd like to onboard to TrueAuth and client-side processing (i.e. one that isn't currently supported by TrueAuth or SmartAuth)? Is there anything that would keep us from being able to onboard a merchant to both TrueAuth and client-side only processing?
A: For clarification: No matter the authentication (TrueAuth or not) card details go to our CDE. Are we on the same page here? For context, we prioritize which ones we move to TrueAuth primarily based on volume. The reason is that since TrueAuth typically performs better from a conversion rate standpoint, and allows us to not collect user credentials, higher volume = greater decrease in credentials + higher impact to overall conversion rate. We typically don’t need inputs from you for a large provider like Chipotle since we can use our own accounts to build the integration. However, if it is a small municipal utility provider, we may need access to a sample account before we could move it to TrueAuth, which we may not be able to get without actually having service from a given regional utility provider. There isn’t a limit - it is just an investment to build the integration over TrueAuth I believe we just clarified this question. See my response to #1 It requires development effort from our team. Our roadmap is generally driven by volume to a given merchant, but there are exceptions, such as a merchant representing a disproportionate amount of traffic for a given customer (think a large employer near a credit union), or some other strategic reason.

Q: I am confused on when you say "allows us to not collect user credentials,"  Does that mean in case of long tail merchant you collect user credentials ?  if yes, how and when do you collect this credentials and how and when you send it to your backend ?
A: TrueAuth and SmartAuth are authentication methods. TrueAuth keeps authentication on the device, SmartAuth happens on our baackend, with the user passing credentials until they’re properly authenticated. TrueAuth, an optional feature supported on native mobile version 3.0 or newer of the Transact SDK, creates a direct connection between the user’s device and the employment system. With TrueAuth, the end user temporarily leaves Transact to self-authenticate using the employment system’s website or mobile app. Afterward, the end user is redirected back to Transact to complete the Transact flow and return control to Transact. With TrueAuth, users enable a direct deposit switch, payment switch or income and employment verification without sharing login credentials with you or Atomic. As the account authentication happens on the user’s device, Atomic has no need to ever receive the login information. For SmartAuth, we collect credentials in real-time within our Transact SDK which sends them to our backend to establish the session with the payroll system, merchant, etc. After we’ve completed the session, the credentials are removed.

Q: To Summarize my understanding: For Short tail Merchant , atomic uses only true auth and no auth data is captured by atomic Merchant switching happen from front end. For Long tail merchant , atomic uses only smart auth where  user credentials are captured and used by atomic (till transaction is complete) to perform switch at atomic backend.
A: Yes

Q: just to confirm , we do not capture user name or password in smart auth flow. Right ?
A: We (Atomic) captures credentials in the SmartAuth flow and uses them for the duration of the session (edited)  FWIW, none (zero) of the PayLink integrations  use SmartAuth today - it is only planned as we expand coverage :+1::skin-tone-2: I don’t have the data diagram for PayLink SmartAuth on-hand since it hasn’t been relevant to PayLink, but here is what the data flow looks like for our Deposit Switch product. Really its #5 and #6 that differentiate it from TrueAuth. The user authenticates through Atomic’s API, and we authenticate with the payroll system/merchant.
```

```
Q: We are trying to change the brand color of the following transcat and see no difference in the UI.
A: The branding color modification currently only applies to the button on the consent page, which by deeplinking to the search page, you are bypassing. Once we have an indication of the employer/payroll system, we default to the colors of that system in order to try to more close resemble the login flow experience. We have some work on the backlog to also add the branding color chosen by the customer to be surfaced in a few other points in the UI like the exit confirmation toast, but those have not been taken up by the engineering teams yet.
```

```
Q: sorry if we've already asked for this but do you have documentation of all your errors?
A: https://docs.atomicfi.com/reference/webhooks#tasks__task-failures
```

```
Q: USPS - wondering if this will be supported in the search API in time for our test as this is one of our “default” employers we show as a default on our search screen
A: I figured out why USPS isn't coming back in the search for you. USPS is TrueAuth only, we have a flag that you can pass in the company search api to allow TrueAuth only connectors. Here is a sample payload of what that would look like. If it is set to false, we won't show TrueAuth only connections in the event you are building out a desktop experience. {    "query": "usps",    "products": ["deposit"],    "scopes": ["user-link"],    "canReferToTrueAuthApp": true}

Q: we don't have a desktop experience just mobile so canReferToTrueAuthApp should be true.  What is the scopes field and what other possible values does it have?
A: user-link is for the deposit product, pay-link is for our switch product (card switching)

Q: is it required, considering the deposit product is specified?
A: I think there is some backwards compatibility however this is the best method to ensure no other companies are returned for other products. The other user-link product we have is the verify product
```

```
Q: hey atomic team! we haven't been able to successfully submit a switch in prod. when i tried, i got this screen. is this just in the case of a longer than usual switch processing time? what is the likelihood that this switch actually goes through? when the user exits the automatic flow we typically show them a message to try manual if it was unsuccessful or to confirm the switch worked and what to expect next. it's not clear to me what we should be showing after this experience.
A: I know we’re still working on the Justworks updates to address the issues Current was having. We are still iterating to make the experience more streamlined. In the event something isn’t automated we have a fall back that can take up to 15 minutes to complete or fail. You will receive a web book with the status. My team is working on fixing just works.

Q: glad to hear you're working on fixing it! any idea the % of jobs that complete vs. fail? that will help us determine where to bring the user next
A: About 3% of our traffic gets hits this screen in a given month. The success rate avg is ~32% from this screen to the task completing successfully. From a UX standpoint, it is ideal to listen to the webhook and notify the customer. I would still recommend taking them down the manual path as a backup. Most of these tasks complete within 15mins.
```

```
Q: question regarding the POC. we have our own search experience and manual fallback. is there anything we need to do on our end to disable these features for our POC?  for manual fallback, our client engineers think they disabled it but we don't have a way to test it yet. we think of manual fallback as if the user leaves the automatic switch flow, you prompt them to switch via a form or other method. we have our own fallback so don't want to be repetitive. can you confirm how to disable this?
A: For the manual fallback, you would want to use our manual fallback CTA setting. You can enable this in console. We do have an atomic version of the pdf manual flow but you won’t need that. The “Set up manually” CTA will be shown whenever the user goes to leave or runs into an error. I’ll make sure our version is disabled.

Q: for search, my understanding is we can pass the platform to go directly to that auth page but when the user clicks back it goes to Atomic search. can we make that screen say something like are you sure you want to return to current? or just disabled the back button for that screen only? i’m testing on version 3.7.18 of the iOS SDK, and i’m seeing that by default when deeplinking into an employer, the back button is still visible and takes me to the search screen. I see a way to hide the back button in the SDK, but then it hides it for other screens that are navigated to. Is that expected? when I pass showBackButton as false it hides it but i’m not sure if that’s going to hide it for every screen, preventing the user from going back without exiting the SDK. same thing is happening on Android as well
A: We are going to implement a change so it works properly for your use case. I’ll keep you updated on progress since we want to get this out early next week prior to your go live. The current way it works is: defaults to showBackButton: true  which shows the back button even when deep linking.  showBackButton: false hides the back button on every screen (For some use cases where the customer app is handling navigation) Hi we are going to be releasing a fix for this today/early tomorrow. In your case you will not use this showBackButton parameter. A. Don’t pass in anything for navigationOptions showBackButton. When a user is deeplinked they cannot go back to search, the back button is only shown to navigate through the reaming steps of the flow. B. showBackButton: true. This always shows the back button even for deeplinked users C showBackButton: false. This always hides the back button on all steps of the flow.

Q: with those changes, there should be no other way for users who deep link to company to get back to search and/or select another company to link, correct?
A: Correct

Q: Somewhat related but we also see that when completing a successful switch, there is a Set up another account button that takes you back to the search screen. Ideally this can also be hidden to prevent users from going back to search, but I don’t see any configuration for it. We also found that when you submit a gig switch it prompts you to switch another
A: We don’t yet have that CTA as a configurable option but we’re working on making it one. Likely to have this within the next month. However we can hide it on our end if it is a blocker. For context, we released this new CTA back in July and since then have scene a 2% CTR. Of those that click it they convert at 38%. We’ll be releasing the change to hide the set up another account button / gig account carousel on the success screen.
```

```
Q: We are also having some issues with your search. When you search for ADP for example: You get a long tail of results that aren't always relevant
A: The reason for so many results in this case is because the search term "ADP" is so short. To help catch misspellings, we include some fuzzy search results, so with a 3 letter term only one letter has to match. Since those matches aren't very strong, they're ordered primarily by popularity once we reach the fuzzy matches.

Q: Okay thanks. Was there any testing that shows that returning more results performed better than returning the match?
A: Yeah, we found that for longer/more specific search terms especially, its better to include as much as possible, and that there doesn't seem to be a drawback to including extra so long as our ranking/weighting is good enough to keep the most relevant results at the top for less specific search terms. I’d add that this approach benefits the longtail list of employers and encourages the user to try different variation of their query. I agree that it isn’t ideal for “adp”, but typically users aren’t using search for main payroll systems - they are just selecting them from the initial list.
```

```
Q: Our team is working on our integration and needs prod keys. sounds like they are not yet accessible to him through the dashboard. who can help?
A: I have enabled live testing. Let me know when you are ready to enable live mode.

Q: Thank you! Could you explain the difference between live and live testing? We expect to be ready for employee testing in the production environment early next week.
A: Live test tasks are not billable but are limited in quantity (about 5-20).

Q: We're trying to do employee testing and are getting an error "You have exceeded your maximum amount of tasks. Please contact Sales to go live." We haven't been able to try a switch
A: I have reset the maximum amount of tasks. Will you try again? Let me know if you have any issues.
```

```
Q: Hey Atomic team. Are these all the interaction events that we will receive on the client from the SDK? Looks like it's only page views and I don't see any event that would confirm a switch / successful switch. https://docs.atomicfi.com/reference/transact-sdk#event-listeners__interaction-events
A: There are quite a few more than this. The best way to see them all in context is to use the Emulator in our Console. You can also expand the events to see properties.
```

```
Q: Do you support true auth for long tail merchant ( merchant switch happen at backend) but atomic do not capture user credentials ?My understanding is that long tail merchant only support smart auth . Ture auth can not be supported unless merchant is converted to short tail  (front end switching) is that right ?
A: Long tail in my mind is not a term related to the technical nature of the merchant - all it means is that it is in a long list of merchants with very low volume (such as regional utility providers). ------ That being clarified, it is possible to support these merchants over TrueAuth (there isn’t a technical restriction), but we may not launch them this way for two reasons: We need credentials to build the initial integration for TrueAuth. Obtaining credentials to test the electric company for a small city is going to be difficult, if not impossible. Maintenance of thousands of integrations can be expensive for TrueAuth if the volume is low since they can be more difficult to debug/test. For these long-tail merchants, it is more reliable to build them not using TrueAuth. In summary, it is theoretically possible to launch every merchant on TrueAuth, but it doesn’t make business sense for the bulk of these long-tail merchants from a cost & delivery perspective.

Q: Our leadership is taking a look at the method by which we store card credentials at the merchant. I think this keeps getting conflated with the method by which Atomic authenticates with the merchant (TrueAuth vs SmartAuth). In a thread on this channel you clarified that these two things are not related (i.e. at a merchant a customer could log in using TrueAuth but have their card data stored using the CDE environment). There are two separate decisions we are trying to make internally - 1) do we want to use TrueAuth, SmartAuth, or both to allow our customers to authenticate at a merchant and 2) do we want to use the CDE environment to store customer's card credentials at a merchant or continue to explore the option of keeping it client-side only when storing card credentials. Though there are similar impacts to these decisions (namely, the amount of merchants that can be supported with each) these are ultimately decisions that are independent of each other.
A: This is helpful context. In the case of TrueAuth, it is accurate to say that these two things (card data treatment and authentication) are technically independent of each other. The following does not apply today, and won’t apply until we launch merchants that don’t use TrueAuth: When we are not using TrueAuth, the card data is not transferred over the client side since there is no client-side connection to the merchant. Our CDE is the egress for these calls to the merchant and so card data must pass through CDE for these card switches to be successful.

Q: Gotcha, so we couldn't have a Smart-Auth merchant that stores credentials using a client-side connection?
A: Not today, and we don’t have plans of building that.
```

```
Q: Is there a way to implement IP Restriction from Console? Is there a way to whitelist IP addresses from Console?
A: We don't currently offer IP restriction if the customer uses native authentication controls for Console. However, you can enforce IP restriction by using your own Single Sign-On (SSO) solution / Identity Provider (IdP) that enables it. Many of our customers use this approach. By using an IdP you can implement IP allowlisting to securely manage access.
```

```
Q: What is MuppetIOS and QuantumIOS? Are those needed along side AtomicTransact?
A: MuppetIOS is a sub-dependency of AtomicTransact and is required to be added in order to use the Atomic SDK. The reason for this is that MuppetIOS contains the TrueAuth framework, which is an internal package that AtomicTransact depends on. With the most recent SDK update version 3.8.0, QuantumIOS is now required as well. This is all bundled in for you when you install the SDK. So the three "frameworks" you see in your code is AtomicSDK, QuantumIOS, and MuppetIOS.
```

```
Q: I have a question about webhooks .. I assume that Atomic will be sending only events specific to Capital one customers to the Webhook api endpoint . Is that assumption right ? How does Atomic filter CapitalOne customers ?
A: That is correct. We use the API key to segregate the traffic internally so we'll only send webhooks for Tasks associated with the API key in the associated Atomic env (sandbox|prod)

Q: To be clear, there's a separate API key for each environment, like prod and sandbox, correct?
A: nope. one API key per customer. the URL of the API itself is what determines the env. sandbox tasks go through sandbox-api.atomicfi.com and prod api.atomicfi.com
```

```
Q: We’re trying to get some claims substantiated (ensure that what we tell customers are true/backed by numbers). For the phrase “Updates may take 1-2 pay cycles to take affect.” does Atomic have disclosures that quote this or data we can use as reference?
A: When an end user successfully goes through the Atomic flow it is immediately written into the payroll system and reflected there. The reason for the 1-2 pay cycle disclosure is a payroll is usually "run" in advance of the actual pay date. For example, if I was paid tomorrow the cutoff might have been Tuesday evening for our HR department to finalize (run) payroll. If I switched through Atomic today I would have missed that cutoff, even though I am not paid yet. Therefore, I would not get paid not on my next cycle (tomorrow), but the following one in two weeks.We put in the disclosure based on our knowledge of how payroll systems generally work and to let the end user know it might not be their immediate next pay cycle, but the next one.We don't track when an account actually funds because we don't have visibility into that side of things (and therefore wouldn't have concrete data on this). It would be something Capital One would have to do the tracking for, if desired. In this case, it's rare that a customer would track number of pay cycles to fund and would more likely be "days to fund".
```

```
Q: We learned last week that Atomic has socket connection between SDK and atomic backend. We also learned that atomic send card data from DCE to Device in plain text in case of non long trail Merchant. (please let me know if this is not right understanding) . Question -  Do we use create another connection or use different method  to send card date from atomic to SDK or do we use same socket connection established for other communication to send this data ?
A: Yes we have a socket connection between the SDK and Atomic, but it is not used for card data. Data transferred over TLS is not plain-text - it is encrypted. This is the same approach for data being sent to the merchant, regardless of integration strategy. This is an API request from the device to our CDE to retrieve card data.

Q: When we send card data from customer to CDE using user end point , is there a way  we will able to encrypt it at field Level  (and get decrypted at CDE) or will it be just post submission over HTTPS?
A: Currently, this is over TLS without additional layers of encryption. It wouldn’t be difficult to add field level encryption, with the caveat that it could not use our KMS instance since the CDE is entirely separate and hosted within Basis Theory, without access to our keys.

Q: Is card data is transferred   though api call from sdk to atomic-backend over https?
A: Yes, but when reference atomic-backend this call is not sent to our regular API. It is issued to our CDE.

Q: Is card data is transferred  though api call from atomic-backend  (CDE enviornment) to SDK in case of non long tail merchant?
A: Yes

Q: When customer backend make a call to user endpoint to submit card data , its api call over https?
A: Yes - this is a call from customer -> Atomic CDE, using TLS.

Q: During the onDataRequest() callback, card data is transferred to CDE by C1 --> we would encrypt this the same way we do with bank data today (field level encryption)
A: It is not possible to do the same way we encrypt bank data, using KMS. We can still use field level encryption but we’d need to manually generate/manage the public/private key pair since it is within Basis Theory (not the AWS environment in which we have KMS deployed).

Q: Once the Card Data is available in CDE, the SDK pulls that from CDE --> my understanding was this data has to be decrypted before sending to client, because the client directly sends it to the merchant via an API. Are you saying the data passed back is still encrypted? If so, is it decrypted before sending to the merchant on device?Or, are you saying the SDK calls CDE again with the merchant API request as a proxy for the data to be decrypted and sent to merchant?
A: It is detokenized in the CDE and sent to the user’s device, encrypted over TLS. It is then sent to the merchant encrypted over TLS.
```

```
Q: Can Atomic support on customer's root certificate pinning in webview?
A: We don’t support this today. There are three systems that the SDK talks to: Our API (non-sensitive data) Basis Theory (for card data) The merchant (for updating cards) Which system are you referring to as a candidate for cert pinning?

Q: It will be nice we if we  have for all 3 . I know 3 might not be possible. Right ? How about 1 and 2 ?
A: Right, 3 is not possible. Possible, but it’d be a large undertaking for us for a number of reasons - mainly having a different version of our SDK, implementing it in general, and the maintenance overhead of rolling expiring certificates. We’d have to coordinate with Basis Theory - I’m not sure on this one. We don’t own this infrastructure ourselves, so we may be limited on what we can do. #1 seems like the most doable, although expensive, but also the least valuable since it doesn’t touch card data.#1 seems like the most doable, although expensive, but also the least valuable since it doesn’t touch card data.
```

```
Q: I want to clarify my understanding of the Terms a customer must agree to. I understand that there are two levels of consent a customer must give: Consent for us (the customer) to share data with Atomic This only has to be confirmed the first time a customer uses Atomic to save their card on file. Consent for Atomic to share data with the merchant. Does the customer have to agree to the Atomic -> merchant consent for each new merchant, or does it apply to all merchants? For example, if I use Atomic to save my card to Amazon I would agree to us (the customer) sharing my data with Atomic and Atomic storing my card at Amazon. If I then want to save my card at Walmart would I have to consent to Atomic sharing my data at Walmart? Or did the previous consent (to store at Amazon) cover that?
A: The first consent covers subsequent connections to merchants and does not necessarily need to be gathered a second time. The first consent is between the user and you (the customer), and is not our requirement. The second consent is our own and is just between Atomic and the user.
```

```
Q: it look like atomic has api hosted  in different  environment  than card data environment . Can you please help me to understand exact flow of long tail merchant here . Does card environment has api which make a request to Merchant ? 
A: Yes the card data is hosted in a completely separate environment.

Q: Or its API who requests merchant by pulling card data from card environment?
A: With some long tail merchants, we may have an API request to update card data on the merchant. This request proxies through the CDE. Inside of the CDE, card data is added to the request before it is sent outbound to the merchant (push not pull).

Q: Also I see the device call to merchant only for authentication , does that mean even for  non long tail merchant , device go to api to make a switch ?
A: This diagram only illustrates the long tail approach. In the TrueAuth approach, the device detokenizes directly with the CDE and an API request that includes the card data is then sent from the device itself to the merchant.
```

```
Q: if someone wanted to contribute a little extra to their account one month, I'm assuming they would just have to log in and increase their deposit amoung prior to their upcoming paycheck, correct?
A: Yes, they would have to go through again. This would apply to all the following months, after this update as well. It wouldn’t be for just one month.
```

```
Q: we received the following message from a user that is trying to connect to her payroll provider. This is one that we haven't seen yet. "Deposit Amount Rejected. Your account does not support the requested deposit amount or there are conflicting allocation amounts"
A: This is a distribution not supported fail reason.

Q: So does that mean there is an issue with the payroll provider (gusto)?
A: Gusto requires that if a user has their account set up for 100% distribution, it won't allow for a fixed amount distribution. Users must choose either a percentage or a set amount for their distributions, but not both at the same time. Does that make sense?

Q: One more question - is the 100% distribution set up by the company or individually by the user?
A: The 100% would have been set up by the end user. What they can do to make it work, would be to change their 100% account to an entire balance/total account. Then they can try again to add the distribution.

Q: From the user: "Do you mean at this point in setting up direct deposit on the Donde website, I need to select a different option than the $25 specific amount? And this is due to having Gusto set up as 100% distribution to my checking account for direct deposit? Thanks so much!"
A: It's ok! She will need to log in to Gusto and change her 100% to the “entire balance or total”. Once she does that, she will be able to add the $25 through Donde and Atomic.

Q: This is directly in her Gusto portal? Is that under a certain page in that account?
A: It is. From the Wallet tab of your Gusto account or the Gusto Wallet mobile app, 1. Select Paycheck splitter 2. Select Edit 3. Select the bank account that you’d like to change and adjust the amount or percentage 4. Save
```

```
Q: What happens when a user sets up a payroll deduction, but then that user goes on leave and they are temporarily not receiving a paycheck. Will they get an email letting them know that the deduction did not go through? Will your system recognize that there is no paycheck to pull from (especially if there will be at a later date)? This company apparently has several employees who take seasonal breaks.
A: Depends on the payroll system and what they do. They will get an email if the payroll system is setup to send out an email when a user gets a paycheck. Otherwise, I assume it would just go through as normal when they get paid again. We don’t currently have a method to track this with our deposit product. I don’t know how Donde recognizes this though. What happens when you don’t get a deposit for a period of time? Atomic just sets up and saves the DD within the payorll system. But we don’t control how the payroll system sends out DD.

Q: help me understand so I can let them know- If I connect my payroll, but next month, I don't receive a paycheck, the connection remains, but no funds are transferred? And there is no way for you or us to see why a payment wasn't received? And just to confirm, if the following month rolls around and I do receive a paycheck, I won't see two withdrawals, that first month was just skipped right?
A: I won’t say for 100% of systems, I can’t guarantee that. But if an employer has known seasonal employees, then the connection should remain for all the scenarios I have seen. You should just see one, but that depends on how the employer runs payroll. For most scenarios I bet that the employer will just not process the payroll for that employee for that one month, and then process it again the next month. We do offer another product (verify, where you can pull back payroll system data, you could pull the paystubs for that user if you needed. But in terms of payment received, we do not have visibility into whether or not you receive a payment, that would be on the Donde side.
```

```
Q: What’s the user experience when they click “no thanks”? Are they sent through the standard auth flow, which then fails?
A: Yep, they would just be directed to the standard login page. In the case with Paycom, it will most likely fail. We know due to their MFA flow, that trueAuth outperforms standardauth. If the user was on a mobile app they would have the trueAuth experience by default (this is why we need the QR code and app clip flow for desktop users). If you are working with a customer that uses ADP as their payroll, it is most likely that standard auth would work perfectly fine as well though. So it will be payroll specific whether we know trueAuth outperforms or not. Looking at some of the new tasks coming through. So the positive is, that we know this will work with trueAuth. But if a user selects “No thanks” from the screen shot below, it is unlikely that the user will convert with Paycom unfortunately. For your own troubleshooting, you can check the Webhook Events
```

```
Q: from your last chat, you mentioned you’re gonna send us documentation on adopting paylink - and how we can pass the encrypted card pin over to atomic. Are you able to share those over?
A: "Transmitting Card Data" section - "Option 3: BaaS Integration". https://docs.atomicfi.com/products/switch/implementation#overview
```

```
Q: hi Atomic team, we want to check with you currently is there’s any upper limit on the direct deposit amount that user can key in from this screen ?
A: No, I don't believe there is. However, you can set an upper limit within your "Features" tab to prevent users from proceeding above a certain amount. This limit can be a hard or soft limit, depending on whether you click the "Enforced" button.
```

```
Q: Hi team, we wanted to ask if it is necessary to have only 1 guid per customer or account, or can we have multiple guids per single user?
A: Technically we don’t stop you from having multiple per user, but we will send webhook events back to you that include the identifier that you send us. Additionally, if you’re hitting our API, you’d use the identifier to grab data about a particular user. Using different IDs for the same user could make this complicated later on. Additionally, from a data sharing perspective, Atomic tracks a single user across multiple tasks to look at behavior (multiple attempts, various fail reasons, linking multiple employers, etc). We will not be able to track this data without a single Identifier per unique user. We also use this identifier for troubleshooting purposes. Just to point out another consideration.
```

```
Q: Hi team, wanted to ask if task id is common for a session (from token request to success of direct deposit) or taskworkflow id is common per session?
A: you will always receive both. A task workflow will always be created whether you only have a single task or need to create multiple tasks (e.g. run a deposit followed by a verify task). Each task created within the task workflow will have its own id as well. The relationship between task workflows and tasks is one to many.

Q: also, is it possible to include some 'echo' data/metadata  in requesttoken, which can be echoed by webhooks?
A: definitely! Under Transact's Parameters section there is a list of Optional Properties where you'll find metadata which serves this exact purpose. The "Sample SDK Parameters" on the right side of the page has an example in it as well.
```

```
Q: Hi, wanted to confirm events we'll get for each direct deposit action i-e exchanging a token to load the UI and  user action completion would result in following web-hooks being sent to url we'll register: Task status updated - 2 events:  processing failed/completed Task status patched - if the final status was updated (rare cases) - 1 event The schema for the events will be same [https://docs.atomicfi.com/reference/webhooks#tasks__task-status-updated]
A: That's correct!

Q: are any fields optional in the schema.. wanted confirm properties in the event.data obj
A: For a basic deposit task, the only fields that might not be included are metadata and distributionAmount. Metadata is only included if it is set in the Transact config object, and distributionAmount won't be included in the event of a total deposit switch

Q: I see..we had planned to rely upon metadata.<custom_field> which will help identify something at our end in addition to the guid. Is Transact config object set when configure the integrations or we pass it in when we request for the token?
A: When you configure the integrations. What are you trying to identify? Passing in additional tracking information is a fairly common use case for metadata

Q: thanks great, yes additional specific info which will help us avoid redundant lookups at our end. I'll make a note to request configuration of Metadata to be included. could you please help us understand how we can configure the Transact config object
A: When you open transact in your code, you need to pass an object in to the Atomic.transact() method that has all the the customizations you want for that instance of transact. Here's an example of what that object might look like:  {  "publicToken": "PUBLIC_TOKEN",  "tasks": [    {      "product": "deposit",      "distribution": {        "type": "fixed",        "amount": 50,        "action": "create"      }    }  ],  "theme": {    "brandColor": "#1b1464",    "overlayColor": "#CCCCCC"  },  "deeplink": {    "step": "search-company"  },  "language": "en",  "metadata": {    "version": "1.2.1",    "test": "New User Experience",    "testVariant": "B"  }} When I say configure the Transact config object, I mean passing the parameters you want into that object. You can read more about our Transact parameters and how to launch it here: https://docs.atomicfi.com/reference/transact-sdk#parameters

Q: I see, so looks like the UI will be one invoking Atomic.transact() is there a way we can set metadata when we request the token?
A: Currently there isn't, customers typically set the metadata in the front end. 
```

```
Q: Where can I find the IPs/domain we can call in both sandbox and production, to request a token?
A: They're listed at the bottom of the access token sample code (https://docs.atomicfi.com/reference/api#access-token) in our docs, and I'm also listing the URLs you send a post request to to request a token: Prod:  https://api.atomicfi.com/access-token Sandbox: https://sandbox-api.atomicfi.com/access-token
```

```
Q: could you please help us understand if publicToken fall under sensitive data, having it logged or stored in clear text would have any security concerns?
A: the public token is a uuidv4 separate from both user and customer identifiers so does not represent a sensitive piece of information.

Q: Also if someone gets hold of this value.. what actions would be potentially permitted? For eg: the UI sdk can be loaded using this value - could that be a concern or any apis which can be invoked permitting any actions using this value alone?
A: The public access token can not be used for any sensitive data retrieval endpoints. Any endpoints for retrieving sensitive data require your api key and secret. (https://docs.atomicfi.com/reference/api)
```

```
Q: I think you had mentioned we could request for retries, wondering if there was a programmatic way to request for them?
A: We retry endpoints up to 3 times with a 30 second interval between retries. Any non 200 response will result in a retry. This includes if the registered endpoint is unavailable. If you have webhook events that you missed, we have a means of resending events on our end. If you provide us any of the following, we can have webhooks resent: Task IDs User Identifiers (the value you pass us as identifier when creating an access token) Start date and end date

Q: Is there an automated way to trigger this? Like say we identify an outage from t1:t2 we could hit a url passing these to get the events replayed? Also if we have to reach out would slack be the best way or any other communication form is preferred for these interactions?
A: we don't currently have an automated way to trigger replay of webhook events. Slack would probably be the best way to reach out. I checked in with our Customer Success team yesterday and the ability to self-serve re-sending of webhook events has been a request from other customers, too. We've noted yours and others' interest and will keep you updated on any developments.
```

```
Q: Hi atomic team, I see that there are some changes to access token method: link (https://docs.atomicfi.com/reference/api#access-token__create-access-token), is this different from https://docs.atomicfi.com/products/deposit/implementation#authentication? can you let me know if we'll be able to set token expiration time as expiration time is optional property in link (https://docs.atomicfi.com/reference/api#access-token__create-access-token)  (if there is example of the format of this, let me know) there are other variables in access token request body, can you provide a bit more details about each:"identity": {    "email": "example@atomicfi.com",    "firstName": "First",    "lastName": "Last"  },  "paylink": {    "accountNumber": "YOUR_UNIQUE_ACCOUNT_NUMBER",    "totalPayments": 36,    "paymentsMade": 0,    "amount": 500,    "paymentDay": 5,    "allowPartialPayment": true,     "firstPaymentDate": "2022-01-15"   }
A: We just launched some documentation for our new product, Paylink, and it looks like the general Create Access Token document is a bit confusing now. We'll get that clarified. In the meantime, since your use-case is for the Deposit product, following this example is your best bet: https://docs.atomicfi.com/products/deposit/implementation#authentication The tokenLifetime property can be included in the payload. Clicking the arrow next to the parameter will show its details (see the attached screenshot). The identity and paylink properties are only for our Paylink product.

Q: just to confirm, is tokenlifetime available for deposit product?
A: yes, it can be included in the payload for a Deposit token.

Q: could you also share the limits for this field? (in seconds, what are the min and max values that can be allowed) also, the response doesn't include this field, would it be possible to include this in the response?
A: we have a minimum of 1,800 seconds and don't have a maximum specified in our data model, though we use Node on the back end and therefore would have a limit of the maximum integer size in Node. However, it's recommended to create a new access token every time you instantiate Transact, so access tokens should be short-lived. Are you interested in the value of tokenLifetime, so the number of seconds that was passed in? Or a date when the publicToken will expire?

Q: thanks, this info helps. yes, wondering if it's possible to include the datetime (with seconds precision) in the response?
A: I'll take note of your interest in this and keep you updated if we make this change. Please note, however, as mentioned above that a new access token should be created every time Transact is instantiated, so it's not recommended that tokens are reused.
```

```
Q:  Could you tell us how to onboard a new client on Atomic?
A: But this is essentially the process today: Email or slack Atomic with the name and logo of your new client. He will create what we refer to as a child account under your parent account within Console. You can then retrieve the new API key and secret under “Settings”. You should be able to see what it will look like today within your Console. I have set you up with Galileo as your parent account and Test 1 and Test 2 as your child accounts.

Q: Do we always have to go through Atomic for this? Is there anything we can do to onboard the client ourselves?
A: We are exploring ways to create an automated self serve process. However this is our only process currently.
```

```
Q: Hi atomic team, wanted to check if webhook publishing is working or not, since I put a dummy webhook from webhook.site over here-  and tried sandbox credentials for url = 'https://sandbox-api.atomicfi.com/access-token', which gives me success response with token, but no event is published to webhook.site to check if webhook.site is working or not(thought that maybe whitelisting is the issue), I send a dummy event using 'send a test event' part in atomic console (seen in image below), and it shows the test event. Can you let me know if some settings are wrong, or just that atomic does not send events for request token - but sends events when deposit starts?
A: We only send webhook events once deposit starts, that's why you don't see them when you generate a token. Since your dummy webhook was able to receive the test event, you're good to go!
```

```
Q: Hi Atomic team, could you please help us understand which all failures would apply for direct deposit switches from https://docs.atomicfi.com/reference/webhooks#tasks__task-failures
A: all fail reasons apply with the exception ‘no-data-found’
```

```
Q: Do we have any documentation on how our clients could integrate with the the Atomic SDK?
A: We do - you can find it here (https://docs.atomicfi.com/reference/transact-sdk)
```

```
Q: Hi Atomic team, for the ddswitch events.. we have seen following types of events when we run thru the simulator: Task status updated [event.data.status = queued & completed], Task authentication status updated [event.data.status not present} Wondering if (2) Task authentication status is expected & should we have the status with it (docs dosn't list the status attribute), but our understanding from prior discussions was we'll receive only (1) Task status updated Could you please confirm this?
A: The Task-authenticated-status-updated (https://docs.atomicfi.com/reference/webhooks#tasks__task-authentication-status-updated) is expected. You will receive a true or false in the data on these events. You are right in your understanding that there will only be one Task-status-updated (https://docs.atomicfi.com/reference/webhooks#tasks__task-status-updated) event. The possible responses under status here are failed and completed. You will only see the “queued” response for previousStatus not status on the Task-status-updated event.

Q: could you please elaborate on the Task-authenticated-status-updated (https://docs.atomicfi.com/reference/webhooks#tasks__task-authentication-status-updated) status (what it means by auth = true vs false) Wondering what we could infer form & if its of relevance for our clients?
A: It just indicates that the authentication was successful or not. This event will always be true for an event that has a completed status. I believe for your purpose, you can only need to listen to the “Task-status-updated” and you can ignore the “Task-authenticated-status-updated”. But it is up to you. With “Task-status-updated” you will always get the status: completed or a status: failed in the data field. For a failed task there will also be a failReason that specifies what the failure was.
```

```
Q: Hi atomic team, wanted to check if title field is still available in this access token endpoint - https://docs.atomicfi.com/products/deposit/implementation#authentication__request-an-accesstoken-server-side
A: The title field is still available, I'll get that added back into the docs
```

```
Q: Do clients like HRBlock/walgreens need to whitelist Atomic specific URLs?
A: Yes, we have found that clients should whitelist our URLs as a best practice.

Q: Galileo is whitelisting atomic specific URL's , I'm asking prev question again to reconfirm it,  Does end client like walgreens should also whitelist atomic URL's?
A: yes we would recommend that, in case they have any restrictions in place that would prevent their applications from accessing our websites

Q: Can you please provide me the list of URL's to be whitelisted from client's side?
A: [realtime.ably.com](http://realtime.ably.com) [ingest.atomicfi.com](http://injest.atomicfi.com/) [cdn-public.atomicfi.com](http://cdn-public.atomicfi.com/) [atomicfi-public-sandbox.s3.amazonaws.com](http://atomicfi-public-sandbox.s3.amazonaws.com/) [atomicfi-public-production.s3.amazonaws.com](http://atomicfi-public-production.s3.amazonaws.com/) [api.atomicfi.com](http://api.atomicfi.com/) [sandbox-api.atomicfi.com](http://sandbox-api.atomicfi.com/) [cdn.atomicfi.com](http://cdn.atomicfi.com/) [cdn-sandbox.atomicfi.com](http://cdn-sandbox.atomicfi.com/) *.[atomicfi.com](http://atomicfi.com/) [transact-sandbox.atomicfi.com](http://transact-sandbox.atomicfi.com/) [transact.atomicfi.com](http://transact.atomicfi.com/)
```

```
Q: Is atomic SDK same for both CV and prod environment? 
A: Yes it is the same for every environment. When you create an access token with our sandbox API however, the token will be prefixed with test-, but in both sandbox and production cases, you use the same SDK call, just send in a different public token
```

```
Q: Hello team, does the current ADP coverage include Run? This is the ADP small business platform.
A: Yes!

Q: Should borrowers be selecting the base ADP option for that? I didn't see a specific listing for ADP Run.
A: Yes the regular ADP login will cover RUN.
```

```
Q: Hi Atomic team, we are planning on running a test in production environment with a internal test client & test account. Could you please help get the api key & secret which can be used for this test? The test would include fetching the token which can used to load the SDK use the emulator / simulate the webhook events to our registered webhook url (to register prod webhook url we are adding the endpoint in atomic console -> Production Account Settings -> Webhook -> Endpoints similar to how we did in sandbox). I do see an option to create a secret like below, please let me know if I should use that
A: I have upgraded Galileo. You should now be able to toggle to production within Console. Here you can retrieve your production API key and secret. These are limited credentials which can be used for 5 tests.
```

```
Q: Whats the difference between bank account and task account in a Backoffice task?
A: Task Account is specifically the account used on the task, whereas Bank Accounts will list all accounts a user has with a customer

Q: Accounts they have with a specific customer or accounts they have on file in their portal?
A: Accounts they have with a specific customer. The User section pictured is populated from the user data passed to us from the customer

Q: so like if a user is a chime user and they have a savings and checking account, both show up in bank accounts?
A: yeah exactly. The task account section was only added to make task auditing easier for QA
```

```
Q: Issue: Tester set up fractional $50 to sav and completed the switch.  Realized they made a mistake, went back in and selected "modify" to change to checking. Looked in ADP and both reflected. I explained (from experience with RCU and Atomic feedback) Atomic cannot remove an account on file.  Depending on the payroll system, Atomic can change the total and move the acct to $0. COMFIN had detailed feedback to my answer-in which I will list here in full form: We can talk it out at our next call, but I'm not sure your response makes sense to me. The word "Modify" would indicate that you are changing what you already have setup. If Atomic can't do that, then the option shouldn't be there. To your point, if it was one of the cases of the Full Payroll (which I do appreciate is 85% of the time) then I suppose the Modify is if you want to direct the deposit to another deposit account? If that's the case then Atomic really needs to build in some logic to identify when it is a full switch vs a fractional and present options accordingly. Because in the case of customer X, she gets the green "Updated" confirmation message. The account number above changed from her savings to her checking indicating the change was made (attached again for reference)... And on the that same screen, it shows only one Switch has successfully been made. (Compare to the 2nd screenshot from UAT showing multiple for comparison). So customer X is going to think...Cool...my $50 is all set, and will be very surprised when $100 comes here; $50 to checking, $50 to savings. See what I mean?
A: Thanks for sharing. There are a couple of issues going on here: #1 Our task history screen has an outstanding change that we are working on. It has to do with our logic for grouping accounts. Currently it is grouping tasks based on the payroll system. We need to have it group based on the account number and employer so it will show these as two separate tasks. #2  The modify button does allow the user to go modify the amount however, it doesn’t allow them to remove the account or set it to a $0. Removing accounts is a limitation of our system that we may support in the future. I think this is a good point from their end. An improvement we could look at making soon is this. When a user clicks modify, we could allow the user to select the account they want, confirm the amount, and then run this task as an override. Update: #1 We are updating our task history / return user screen to properly reflect tasks for when setting up different accounts on the same payroll provider #2 ADP Pre-note verification: Our ADP contacts are unable to share the exact percent of employers with this enabled. They did claim it was a fairly small portion of their employers. On a positive note, our ADP CoAuth integration will now completely bypass any prenote settings.

Q: Where does Atomic stand on prenote verification
A: I believe the stats on prenote verification will drive if the FI feels good about just using the disclosure available in Lumin, or if a speed bump is really necessary for launch. (which a Lumin speed bump they would be waiting on DEV unless Atomic can read there is a prenote in the comms and then build out their own speed bump). ADP users that were issued checks from previous payroll did receive direct deposit on current payroll. Atomic is piloting a prenote override with ADP which also allows the user to see all the related accounts defined within ADP for allocations. Atomic has researched and found in the comms there is a way to recognize if the payroll provider has prenote requirements. DEV work to add this into the workflow and provide the user a speed bump will take about a month on the Atomic side
```

```
Q: This is a long shot but do you have any context of how common the ADP Pre-note verification is? We had a customer get a paper check and said they’re company has prenote verification enabled.
A: I’m not sure but I think it definitely has to do with what ADP system it is behind the scenes. This is almost the opposite of the issue Earnin had where their HR team declined the change because we did it in such a way that would override pre note. I think at some point there was a flag that I thought we were using to try and override it on purpose. I’m also confused why they send a paper check while it is happening. Maybe we can ask the ADP team about that and clarify if via CoAuth it will bypass it since we are sending it programmatically to them. Our team is working to make it so CoAuth bypasses this since the update request is coming directly from the bank similar to how plaid verification is instant. I’m wondering if we can detect this and let the user decide to proceed with the update or atleast tell them on the success screen. Even if they were to update it directly in ADP today they would get a paper check.
```

```
Q: Question came from Lumin who re-sells DD based on feedback from their client's testing.  Would love any insights that could be shared to answer the questions. COMFIN tested ADP, where they had a setting on the back end requiring prenote verification which caused a paper check to cut. Had the member changed DD directly in ADP a pop-up message would have told them about the paper check. FI was asking for feedback from Atomic regarding other companies that have this optional additional verification and Atomic plans for how to manage this as well as any insight for other experiences that trigger paper checks.
A: I think we could implement a check for this and communicate it back to the end user. ADP said CoAuth can bypass this since the update is coming from the bank directly. However, they said this is not in place just yet.
```

```
Q: is it possible to launch atomic and not allow partial switches?
A: I believe customers can turn off the Fractional Deposits in Console under Settings, Features, toggle Fractional Deposits OFF

Q: can customers turn off fractional deposits only for specific problematic HR systems or is that global for all?
A: that's a global setting
```

```
Q: Your Paylink subscription service is for debit card switch . It does not track all subscriptions to negotiate costs and cancel things you don’t need, does it?
A: PayLink Switch - Is for switching your payment method (debit,credit,ach) across various merchants, bills, and subscriptions. PayLink Manage - Is for tracking all of the various payments/bills/subscriptions. Users can take various actions on these linked payments to do things like cancel, move payment date, negotiate, etc. This product is still under development. The two can be used independently but interact together when both are used.
```

```
Q: we have a prospect that is asking of the link for atomic can be outside of Digital Banking?
A: Can you provide some more detail here? They are wanting to provide users access to atomic outside of digital banking?

Q: for clarity on this question, the FI is asking because they want to be able to market Atomic using multiple avenues (not just in OLB).  Perhaps using an email blast campaign or a QR code in a branch -- they don't want the user to always have to go into OLB to set up direct deposit.  They will have a per trans fee so how would that work IF the user doesn't go through Lumin?  Hope this makes sense.
A: Without going through OLB we’re unable to know the users account/routing info to make the update. We have been working on an in-branch feature that allows for users to go to a generic link. In this case we have the user key in the account number twice. We have this today but would require a bit more setup. They would integrate Atomic onto a website and we would turn on the in-branch flow for them.

Q: How would the FI get fee’d for this?
A: We haven’t had any reseller customers do this approach but for others each switch is just billed the same as a regular one. No additional cost for the feature.

Q: when you say 'regular' one, I assume you mean the same as a user who transacted within OLB correct?
A: yes
```

``` 
Q: Can a user set up a savings and checking account at the same time under the same task?
A: No.

Q: Can a user setup two tasks in one flow in Transact?
A: No, Atomic can't setup two tasks at the same time yet. I know it is potentially in the works because we are looking at running tasks at the same time. But isn't a thing yet.

Q: So, to be clear, a user could set up two separate tasks, one for checking account and one for savings account, but not both under a single task, correct?
A: Yeah, they would have to leave and come back through separately.
```

```
Q: Our customer is wanting a way to discern whether we directed a user to navigate away from Transact before the end screen was displayed to them using the webhooks. Is there a way for us to add a field to the task-status-updated to indicate if that is true or not?
A: We already have this user.connected boolean. user.connected boolean: indicates whether or not the user was present to view a confirmation of the task's final outcome.
```

```
Q: Hey! the funnel looks off. left some comments in the word doc. can you all help double check that those events will always fire? for example, i see only 84% of users that select an employer see Viewed Login Page or Viewed Uplink Interstitial and I would expect that to be closer to 100%. I've investigated this a bit. Looks like it's happening due to users: Viewed a Manual Deposit Instructions Page, Viewed an interstitial type of page e.g. Social Security or sign in by franchise, Viewed System After Hours Page, Viewed Typehead Search by Configurable Connector Page. What are pages 3 and 4?
A: #3 - Is only for Social Security Benefits. Their website is only available during the day. #4 - This is a step for certain payroll systems that require the user to also select their employer (IE, User works for home depot but selects Workday). For analytics purposes, users who first see the Configurable Connector Page will still get trigger the “Viewed Login Page” event but it will be after they select their employer. Also, the Franchise search will be similar to this. Event: “Viewed Search By Franchise Page”

Q: #3 you mean only available to switch a direct deposit? I was on the website the other night for name change purposes.
A: #3 Correct the direct deposit switching is only available durning the day for Social Security. 

Q: That is so odd. So if I as a user wanted to go switch my direct deposit on their website, I can't or is it specific to the Atomic integration? Is this for all Social Security or only employees or benefit recipients?
A: It is their portal that prevents the update for both Social Security benefits and Social security employees. No idea as to why. We think this may be some strategy to prevent fraud. We also have seen a few customers get their routing number blocked.
```

```
Q: Hi Atomic team, I wanted to flag this crash that we’re seeing on iOS in version 3.8.4 of your SDK. This crash has happened at least 7 times, affecting 5 users according to Crashlytics. I took a look at the instances and in most cases the last interaction event the user sees is Clicked Phone Number From Social Security Manual Instructions , and then they must be tapping something that makes the app crash. In one other instance, the last event they saw was Clicked website-link From Manual Deposit Instructions Page . It seems like there is an unsupported scheme in your webview that users can tap on, leading to a crash. Not sure if this is affecting Android.  We’ve updated the SDK to version 3.8.8 for our next app release, not sure if this fixes anything as there aren’t any release notes, but hoping someone could take a look as I’m not sure if this is affecting more users than what Crashlytics says
A: This wouldn’t be related to any SDK version, and is something we’ll be able to address without you making changes on your end. We pushed a fix out about an hour ago that should address most of these, but we’ll take a look at yours specifically. The issue was that URLs like www.workday.com/pfizer would cause a crash since they’re technically not valid without the https://. We added a validation layer that will fix any incorrectly formatted URLs but we’ll make sure it is covering your case. We also don’t have visibility into these crashes, and so we relied on other customers that brought it up today. Thanks for bringing it to our attention as well. It should have only affected a pretty small segment of your users. 
```

```
Q: Hello Team, we are getting below error while installing the AtomicTransact Framework in our framework : target has transitive dependencies that include statically linked binaries. I guess we need dynamic framework for AtomicSDK to resolve this error. Note - we are using use_framework inside our podfile.
A: we have dynamic versions of our SDK as found here that you can leverage. Built with different versions of Xcode depending on your use case!

Q: I tries using 3.8.5 which was released from here I guess. Still facing same issue while integrating through development pods: Analyzing dependencies Downloading dependencies Installing AtomicSDK 3.8.5 (was 3.5.20) Installing QuantumIOS (3.8.7) Installing RetailDirectDepositSwitchJourney 1.1.2-rc2 (was 1.1.2-rc1) Installing RetailDirectDepositSwitchJourneyProvider 1.1.2-rc2 (was 1.1.2-rc1) Installing RetailDirectDepositSwitchJourneyUseCase 1.1.2-rc2 (was 1.1.2-rc1) [!] The 'Pods-Common-CommonAppDependencies-ProjectName' target has transitive dependencies that include statically linked binaries: (/project_path/Pods/AtomicSDK/artifacts/AtomicTransact.xcframework)
A: in your Podfile do you have any references to static_framework? Also, could you share the line where you include the AtomicSDK?

Q: I  am using use_frameworks! in my podfile. We have created a framework called  RetailDirectDepositSwitchJourneyProvider  and in this I am using AtomicSDK as a pod dependency like this: target 'RetailDirectDepositSwitchJourneyProvider' do   pod 'AtomicSDK', '3.8.5'  end   In my Project I am trying to add RetailDirectDepositSwitchJourneyProvider as a development pod like this - pod 'RetailDirectDepositSwitchJourneyProvider', :path => '/<project_path>/mb-retail-direct-deposit-switch-journey-ios'   and getting the above mentioned error. This I mentioned in my podspec file of RetailDirectDepositSwitchJourneyProvider   s.dependency 'AtomicSDK', '3.8.5'
A: Try this, which points to that specific Xcode15.3-dynamic branch: pod 'AtomicSDK', :git => 'https://github.com/atomicfi/atomic-transact-ios.git', :branch => 'Xcode15.3-dynamic'

Q: I guess we can not use remote branches in podspec file: [!] Invalid `RetailDirectDepositSwitchJourneyProvider.podspec` file: [!] Podspecs cannot specify the source of dependencies. The `:git` option is not supported. `:git` can be used in the Podfile instead to override global dependencies.. When I am using below way, it is working for my framework. But when I try to add the framework in my Main Project as a development pods it is creating issue like mentioned in my previous comment. pod 'AtomicSDK', :git => 'https://github.com/atomicfi/atomic-transact-ios.git', :branch => 'Xcode15.3-dynamic'
A: Ah yes, that stinky .podspec limitation :disappointed: We've come across that in our React Native SDK and it's super frustrating ha. Okay let's see, what's the best way to support you. I could publish a new SDK like AtomicSDK15.3Dynamic, but that is a bit of a pain on our end to maintain, and a pain on your end to update when we have updates. Give me just a minute to bring this back to our team and discuss and I'll get back with you soon. Thanks! if your RetailDirectDepositSwitchJourneyProvider has a Podfile using the AtomicSDK dependency with a branch (which is working), does your main project need to include AtomicSDK as a dependency, or just the RetailDirectDepositSwitchJourneyProvider ? I'd think you wouldn't need AtomicSDK in your .podspec file? Oh, I might be misunderstanding your stack. If you don't mind clarifying, that'd be great :slightly_smiling_face:

Q: it’s an issue with the local dependency management. When I u comment use_framework! it works fine to me in the main project, I will let you know if any future help required
A: sounds good!
```

```
Q: I thought the javascript bridge enabled a totally flexible payload? Is this just to modify an HTTP header, and the native code that sets up that network request? <-- I suspect I know the answer here, but I would like confirmation. What part of the js bridge is flexible versus not? How can we be certain we won't need another version uptick in the near future? (We basically just need more technical information about the problem that requires an SDK bump, as we presented it to C1 Platform as a very bare bones shell that wraps dynamic functionality that could be modified by your backend) Is there anything we can do to future proof changes here so it won't require an SDK uptick in the future for this exact issue?
A: The js bridge is flexible in that we can drive the URLs and conf etc. from our backend; effectively setting the overall flow from our services layer, but the retrieving headers, cookies, etc. from network requests and operating on them is done on the client. That being said, this is not something we've encountered since launching TrueAuth. We've built it to be as flexible as possible so as to minimize the maintenance burden as much as possible, but there are going to be situations which will require upgrades from time to time.
```

```
Q: A customer is going to start with a low fi branch POC and will want to tick and tie back to the end consumer which means we would need to send them back account numbers. Know we don’t do this today. And their risk folks would need to approve. Would also plan to call out within the contract. Any thoughts/strong opinions (maybe sending back the last 4-6 digits via webhooks)?
A: It has this option that we can turn on in Backoffice. "Include Account Information in Webhooks" Include account type, account title and last four of account number in webhooks for deposit tasks. Yep we built this out already. Would just need to turn it on for this customer
```

```
Q: What webhooks should I use for tasks?
A: Depends on the type of task. Different webhooks are used for different tasks.

Q: What webhooks should I use for direct deposit switching tasks?
A: Direct deposit mainly uses task-status-updated (https://docs.atomicfi.com/reference/webhooks#tasks__task-status-updated). There are two others that get sent: task-authentication-status-updated and task-workflow-finished. But these are less important than task-status-updated. When a task-status-updated event is emitted, this indicates that the state of the Task has changed. For example, the Task has gone from processing to failed or completed. If the status is a final status, either failed or completed, no further updates will occur, although in very rare circumstances a task-status-patched event may be emitted. (When eventType is task-status-patched, the final status of a Task was updated. Cases where this may occur are rare and are generally associated with an audit or bug fix within our system.)

Q: What webhooks should I use for verify and continuous access tasks? What webhooks should I use for verify tasks?
A: It depends on whether you're using the push strategy or the pull strategy. Push Strategy: Atomic will periodically refresh a user’s payroll data and proactively push updates to your designated webhook endpoint. Webhook Event: deposit-switch-removed	A deposit switch that was previously added has now been removed. statements-synced	Statement(s) were synced. statements-added	Statement(s) were added. income-synced	Income data was synced. income-updated	Income data was updated. timesheets-synced	Timesheet(s) were synced. timesheets-added	Timesheet(s) were added. employment-synced	Employment data was synced. employment-updated	Employment data was updated. identity-synced	Identity data was synced. identity-updated	Identity data was updated. taxes-synced	Tax data was synced. taxes-added	Tax data object(s) were added. deposit-accounts-synced	Deposit account(s) were synced. deposit-accounts-added	Deposit account(s) were added. deposit-accounts-updated	Deposit account(s) were updated. deposit-accounts-removed	Deposit account(s) were removed. linked-account-connected	A linked account has been connected. linked-account-disconnected	A linked account has become disconnected. task-workflow-finished	The workflow for the user either has completed or failed - includes a failure reason. Pull Strategy: Data can also be refreshed, and retrieved on-demand. Data can be pulled using the following steps: 1) Use our List Linked Accounts endpoint to locate an account for which you’d like to pull data. 2) Pass the linkedAccountId to our task creation endpoint to issue a refresh of the associated data. 3) Once you receive a task-status-updated event indicating that the task status is completed, use our API endpoints to retrieve the latest data, or subscribe to our employment data webhook events.

Q: What webhooks should I use for paylink / payment switching tasks?
A: task-status-updated and task-authentication-status-updated and task-status-patched. When a Task resolves, you will receive the task-status-updated webhook. If the Task was successful, the status attribute will be set to completed. If there was an issue with the Task processing, status will be failed along with a reason attribute containing the reason for the failure.  When eventType is task-authentication-status-updated, the authentication status of a Task was changed. When eventType is task-status-patched, the final status of a Task was updated. Cases where this may occur are rare and are generally associated with an audit or bug fix within our system
```

```
Q: what would project timeline be for an FI that signs this week? Could they be live before year end (in 2 months)?
A: if they were quick with testing I don't see why not...Christina and I scoped Atomic as a 6 week project initially
```

```
Q: Hi Atomic team! I've been trying to integrate the iOS Atomic Transact SDK using the Xcode15.2 branch (running Xcode 15.2) and it looks like the 3 frameworks we're pulling down are AtomicTransact, Quantum, and Muppet. When trying to build the app, I'm seeing this linker error: ld: Undefined symbols:   __swift_FORCE_LOAD_$_swiftXPC, referenced from:       __swift_FORCE_LOAD_$_swiftXPC_$_QuantumIOS in QuantumIOS[3](InternalNotifications.o) I also see this related warning: ld: warning: Could not find or use auto-linked library 'swiftXPC': library 'swiftXPC' not found In Xcode, I can add libswiftXPC.tbd  under Frameworks, Libraries, and Embedded Content, but that file type appears to just point to where the dynamic library should be on the system, and I don't have libswiftXPC.dylib that it's looking for. I thought this was related to my system/the project not being fully configured to actually run swift apps, but apparently this Xcode15.2 version of the SDK does work when running on Xcode 16 :thinkingeyebrows: Also after adding that tbd file, the warning is removed and I get the error showing that it can't find the actual library: ld: library 'swiftXPC' not found clang: error: linker command failed with exit code 1 I'm not sure how upgrading Xcode changes where it's looking for swift libraries, or maybe even which exact swift libraries it uses. I've also tried changing around various Xcode settings based on forum posts, including those related to embedding swift libraries and the specific version of swift being used (4/4.2/5) but haven't had any success. Just to confirm, we do have a swift file in the project that shows up under Compile Sources that sounds like it may be a necessary piece of this. Do you have any suggestions that may help in getting this to work on Xcode 15.2?
A: Thanks for the report. Just to confirm that you've included a Swift bridging file like discussed here? Hey Great news! Here's an example Objective C application that uses the Atomic SDK successfully. It essentially uses Swift to create a bridge between your Obj-C app and our Swift SDK (see the AtomicInterface file and the ViewController file's specifically. Hope this helps get you integrated. Reference: ObjC Demo.zip

Q: I think one attempt did have a bridge file, sorry working on an issue with a repo change to allow me to try that. Can confirm we do have a bridge file, I am seeing the linker error come from AtomicTransact instead of QuantumIOS but the error itself is the same: ld: Undefined symbols:   __swift_FORCE_LOAD_$_swiftXPC, referenced from:       __swift_FORCE_LOAD_$_swiftXPC_$_AtomicTransact in AtomicTransact[3](TransactSheetView.o)
A: Hey! I reached out our iOS dev and he said this: Will you confirm they are using Xcode 16? That’s what the first image sounds like to me, in that case they should be using the main release, not Xcode 15.2. I suspect that’s not the whole problem though. Bridging header was a great question, that would be my next guess as well. Okay another thought, it sounds to me like their project isn’t linking in swift support since they’ve never used swift before, which I’m guessing means this project was created before swift was included by default, so I’m guessing it’s probably just a missing linker flag or something along those lines. I did a quick scroll through what those are and I’m not seeing anything immediately jump out to me as the likely answer, but there is a validation tool built into Xcode that might help. If they open the project file, then go Editor -> Validate Settings, I’m hoping that will show the flags that are missing for swift. They could also try just adding an empty Swift file (Explicitly using “From Template” if they’re on Xcode 16), which really should setup those linking settings

Q: Thanks, I'll take a look at that validation tool :+1: we are using Xcode 16 with the release version of the SDK, but in this case we are working off the atomic Xcode15.2 branch in order to try to make it work specifically with version 15.2 of Xcode. It's possible that this won't work but hopefully so!
A: Yes, try that!
```

```
Q: Is the Atomic's Terms of Use something we can remove from the Transact widget?  The borrower already consented to our TOS (Terms of Service) before arriving at this point.
A: Unfortunately, the Terms of Use link cannot be removed. The Terms of Use link must be placed directly next to the confirmation button for compliance purposes. This specific positioning is legally required to secure the end-user authorization needed to access the customer's payroll system. 

Q: Right but to reach this point in our integration the user has already consented to our TOS that carries the same end user authorization- so this asks it for something that has already been agreed to. Given that can we look at removing this in our integration?
A: Your TOS do not supply Atomic with the permission we need directly from the end user.

Q: We can add the necessary language so that there is only one TOS for the entire experience
A: That doesn't work. There is a power of attorney in the  Atomic TOU that requires us to enter into the agreement directly, as does the Fair Credit Reporting Act. We do not offer a fully whitelabeled version for legal reasons.

Q: Can I get my legal to look at it and offer a suggestion if they find one?
A: I'm a lawyer and would be happy to talk with your legal team. Sorry, but we cannot change this.
```

```
Q: Can a customer customize the Transact screens to remove Atomic's "End User Terms" / "Terms of Use"? Is the Atomic's Terms of Use something the customer can remove from Transact?
A: The link must appear next to the confirmation button (either immediately above or below the button). This is a legal requirement. It is not at the customer's discretion. The customer can't authorize us to access the payroll system. Only the end user can. If we remove the link to the End User Terms, there is no authorization and Atomic may be committing a federal crime (yep, a crime) every time we access a payroll system for that customer. We are not doing the customer a favor by agreeing to remove the link, or by moving/obscuring it.
```

```
Q: Can you share the documentation to set the account type?
A: Our docs are a bit sparse on this topic but your essentially just passing in the key value pair in the metadata field when you initialize transact https://docs.atomicfi.com/reference/transact-sdk#metadata "metadata": {         "data": "test"       },   This is all that is needed for the metadata. Whatever is passed in this parameter is just echoed back in the interaction events

Q: We are passing the data -> account -> type as Savings from the backend when creating the Atomic token.  Just to make sure I understand it correctly - you were thinking of updating this to Checking  to see if the unkown failure rates decrease right?
A: Interesting, Savings was always used? Yes you would be changing this to Checking. The two account type values we accept when creating an access token are checking and savings

Q: Yes. Savings was always used. If we change it to ‘checking’, do you think those payroll system which cares about the account type may start erroring out because the actual account is savings even though we start sending ‘checking’?
A: I chatted with our team on this. There are some payroll systems that do Natcha account validation but none are strict on the account type being set in the payroll system. So we are good to start sending this as checking.

Q: I just verified my direct deposit setup on Workday (for Affirm) and even if we are sending it as Savings from our backend when creating Atomic token, it shows up as Checking account. Any thoughts why would that happen. Also, would I wonder if there is any legal implications if we end up showing Checking  on payroll systems when the account is actually Savings. Any thoughts there?
A: Good question. Let’s put this idea on hold until we know for sure on some of these details. As for the workday account type, I’m not sure why this would happen. Workday lets you select the account type when you change it in their directly. It lets you select savings or checking when doing it manually
```

```
Q: Regardless of providing AI/ML as a direct service, there would be Model Risk Management processes to assess the risk level of any AI/ML associated with a product we will be deploying. That being said, may you provide more specificity around the ML used for the discover features of the payroll login page and of direct deposit/recurring payment requirements of a user’s account? Does it use, for example: Random Forests, Neural Networks, Natural Language Processing, Deep Learning, etc.?
A: First call out to that question; we only utilize ML for authentication. Thus any questions regarding deposit are moot as we currently don’t use ML for any deposit cases.

Q: please clarify. Do you mean that we only use ML for auth so that it's moot for PayLink b/c users login in directly to the third party system via TrueAuth? Isn't ML (SmartAuth) sometimes used on the Deposit side when TrueAuth is not available? When do we use ML?
A: In the world of Deposit, ML is strictly only utilized for authentication when the connector has SmartAuth configured. We don't utilize it for any of the actual Deposit switch logic. In regards to Paylink, it is used for auth and the switching of bank/card data.

Q: So I need answers about (1) discovery of the login page for Deposit,  (2) discovery of the login page for PayLink, and (3) recurring payment requirements for PayLink. 
A: Based on previous answers to questionnaires, we use Deep Learning
```

```
Q: Just got this back from BofA, can we work with this? For Github, use DallasMobileDev. This came back from the Mobile Team. Said it was easier than managing individual GitHub users. Does this work?
A: maybe. I'll have to check, but i doubt we'll have access to the teams in their org.

Q: have a chance to take a look?
A: Using the team from their org is not gonna work. Let me get this set up and I'll can send them a link to fork the repo
```

```
Q: Quick question regarding how parent customers setup new child customers. Is there a reason I can't do this from console for Molecular Bank? I assumed I would be able to to demo, but unsure because I don't see the ability to.
A: Do you see the button in Console under the "Customers" tab that says "Add Customer"? After that, there's a form you can fill out that says "Add Customer" at the top that allows you to designate the Customer Name, Assets in Dollars, Website URL, Primary Contact Name, Primary Contact Email, Logo, and Dark Mode Logo. From there, you can either select "Cancel" or "Add Customer". 

Q: I logged out and logged back in again, and yes I can. Thanks. I think I must have been stuck on my own child account for some reason.
A: good to know
```

```
Q: Do we have a flag to turn on app clip for a customer/connector combo specifically? iSolved doesn’t convert on standard auth, and Donde just signed up a customer that uses iSolved, so wondering if we can toggle iSolved for Donde to app clip?
A: We do. I can set this up

Q: Is connector or company needed? But basically Donde has a customer using iSolved and all tasks are failing because it’s on standard auth
A: We can target all of Dondes iSolved traffic. It looks like all of isolved desktop traffic converts poorly. Probably a good candidate for app clip. We should do another data pull of poor desktop connectors

Q: I would agree. It’s in that original list we pulled for app clip contenders. Let me know when it’s toggled on please so I can update Donde.
A: Alright it should be on now

Q: is this an app clip error you have seen before? Status changed to failed  45ms meta.error JSONRPCErrorException: Cannot read properties of undefined (reading 'url')     at new JSONRPCErrorException (/usr/src/app/node_modules/json-rpc-2.0/dist/models.js:55:28)     at JSONRPCClient.<anonymous> (/usr/src/app/node_modules/json-rpc-2.0/dist/client.js:115:66)    at step (/usr/src/app/node_modules/json-rpc-2.0/dist/client.js:33:23)    at Object.next (/usr/src/app/node_modules/json-rpc-2.0/dist/client.js:14:53)    at fulfilled (/usr/src/app/node_modules/json-rpc-2.0/dist/client.js:5:58)    at processTicksAndRejections (node:internal/process/task_queues:95:5) {  code: 0,  data: undefined}meta.stepIdgather-accountsmeta.flowIddepositmeta.trace{  "traceId": "7064090fe87605718700f43efb637128",  "spanId": "3fed6893f04ad39e",  "dataSet": "queue-processor",  "timestamp": 1723735481}meta.backofficeLogGroup/
A: Thanks David. I have no clue what this error is but we’ll want to look at it. I turned on a few other connectors to appclip to see if we can get any other wins or data. it's something to do with a function being called incorrectly, either it was written wrong or that method didn't get added to the new version. 

Q: With Donde and Rippling traffic does that need to be configured via LD?
A: Yes but Rippling desktop traffic is all behind sent to app clip already. Did they want it turned off? I turned on a bunch of other app clip connectors but none are converting very well. We really need a resources to look at app clip

Q: No, we don’t want it off, I was just wondering how much app clip is behind LD flags vs not.
A: App clips are all managed via LD flags. For deposit, we have it on at 100% for these connectors when trueauth isn’t available: If user connector is one of Paycom, Rippling, Amazon A to Z, iSolved, Namely, TaskRabbit, Insperity, Cracker Barrel, Patriot Software. And if user products is one of deposit. And if user deviceType is one of web. And if user customer is not one of GO2bank, U.S. Bank, Alkami. Serve Deposit App Clip = true

Q: Will we continue pursuing App Clip technology going forward?
A: Only paycom converts well with it for deposit (9.2% as of Nov 5, 2024). There are a number of outstanding bugs that haven’t been addressed and we likely won’t be investing into it more in the near future.
```

```
Q: Hi Atomic team. I'm trying to set up a Manual Fallback for when searching for a provider shows no results: https://docs.atomicfi.com/products/deposit/plan-your-ux#employer-search. I'm curious exactly how I am supposed to implement an event listener using our atomic_interface that is in swift. Does that involve subscribing using syntax that is like this: Atomic.dataRequests.receive(...) or Atomic.interactions.subscribe(...) ? (NOTE: this is specifically for iOS.) 
A: You'll need to react to the .closed event. This will be emitted when the user clicks the button added to the UI when this feature is toggled on (here) in the scenario you're describing. The event will have a "reason": "manual-fallback" value set in it to indicate this feature being triggered so you can navigate them to the appropriate place in your UI.
```

```
Q: Customer Question: What Unemployment systems are covered and what ones are manual? Any additional details you can share on support for government systems / public benefits would be super helpful.
A: All 50 unemployment states are covered. Here is a list of which are automated and which are manual instructions. Name	Name (Connectors) Alabama Unemployment Services	Manual Instructions Alaska Unemployment Services	State of Alaska Unemployment Arizona Unemployment Services	Manual Instructions Arkansas Unemployment Services	State of Arkansas Unemployment California Unemployment Services	Manual Instructions Colorado Unemployment Services	Manual Instructions Connecticut Unemployment Services	State of Connecticut Unemployment Delaware Unemployment Services	State of Delaware Unemployment Florida Unemployment Services	State of Florida Unemployment Georgia Unemployment Services	Manual Instructions Hawaii Unemployment Services	State of Hawaii Unemployment Idaho Unemployment Services	State of Idaho Unemployment Illinois Unemployment Services	Manual Instructions Indiana Unemployment Services	State of Indiana Unemployment Iowa Unemployment Services	State of Iowa Unemployment Kansas Unemployment Services	State of Kansas Unemployment Kentucky Unemployment Services	Manual Instructions Louisiana Unemployment Services	State of Louisiana Unemployment Maine Unemployment Services	State of Maine Unemployment Maryland Unemployment Services	Manual Instructions Massachusetts Unemployment Services	State of Massachusetts Unemployment Michigan Unemployment Services	Manual Instructions Minnesota Unemployment Services	State of Minnesota Unemployment Mississippi Unemployment Services	Manual Instructions Missouri Unemployment Services	State of Missouri Unemployment Montana Unemployment Services	State of Montana Unemployment Nebraska Unemployment Services	State of Nebraska Unemployment Nevada Unemployment Services	Manual Instructions New Hampshire Unemployment Services	Manual Instructions New Jersey Unemployment Services	State of New Jersey Unemployment New Mexico Unemployment Services	State of New Mexico Unemployment New York Unemployment Services	Manual Instructions North Carolina Unemployment Services	State of North Carolina Unemployment North Dakota Unemployment Services	Manual Instructions Ohio Unemployment Services	Manual Instructions Oklahoma Unemployment Services	Manual Instructions Oregon Unemployment Services	State of Oregon Unemployment Pennsylvania Unemployment Services	Manual Instructions Rhode Island Unemployment Services	Manual Instructions South Carolina Unemployment Services	State of South Carolina Unemployment South Dakota Unemployment Services	Manual Instructions Tennessee Unemployment Services	State of Tennessee Unemployment Texas Unemployment Services	Manual Instructions Utah Unemployment Services	State of Utah Unemployment Vermont Unemployment Services	State of Vermont Unemployment Virginia Unemployment Services	Manual Instructions Washington Unemployment Services	State of Washington Unemployment West Virginia Unemployment Services	State of West Virginia Unemployment Wisconsin Unemployment Services	Manual Instructions Wyoming Unemployment Services	Manual Instructions. We support the large federal benefits: SSA, VA Benefits, the major government payroll systems, as well as some state and teacher benefits and retirement systems. And all 50 state employee systems (some using manual instructions) Name, Advisory Council Historic Preservation, Alabama State Employees, Alabama Unemployment Services,Alaska Division of Retirement and Benefits, Alaska State Employees, Anniston Army Depot, APERS, Architect of the Capitol, Arizona State Retirement System, Arizona Unemployment Services, Arkansas State Employees, Arkansas Unemployment Services, Armed Forces Retirement Home, Army and Air Force Exchange Service, Army National Guard, ARTRS, California State Employees, California Unemployment Services, CalPERS, CalSTRS, Centers for Disease Prevention, Civil Service Retirement, Civil Service Survivor, Colorado PERA, Colorado Public Employees Retirement Association, Colorado State Employees, Colorado Unemployment Services, Connecticut Retirement Services, Connecticut TRB, Connecticut Unemployment Services, Defense Health Agency, Defense Logistics Agency, Delaware Unemployment Services, DFAS myPay, District of Columbia Retirement Board, District of Columbia Teachers Retirement Plan, DPERS, ERS of Texas, ERSGA, ERSRI, Farm Credit Administration, Farm Service Agency, Federal Deposit Insurance Corporation, Federal Emergency Management Agency, Fire & Police Pension Association of Colorado, Florida Retirement System, Florida Unemployment Services, Georgia Unemployment Services, Government Accountability Office, Government Printing Office, Hawaii Employee Retirement System, Hawaii ERS, Hawaii Unemployment Services, Idaho State Employees, Idaho Unemployment Services, Illinois State Employees, Illinois Unemployment Services, IMRF, Indian Health Service, Indiana Child Support, Indiana Laborers Pension Fund, Indiana Unemployment Services, INPRS, Internal Revenue Service, Iowa Unemployment Services, IPERS, Joint Chiefs of Staff, Kansas Unemployment Services, Kentucky Child Support, Kentucky Unemployment Services, KPERS, KPPA, LASERS, Louisiana Unemployment Services, Maine State Employees, Maine Unemployment Services, MainePERS, Maryland SRPS, Maryland Unemployment Services, Massachusetts PRIM, Massachusetts Teacher Retirement System, Massachusetts Unemployment Services, Michigan Office of Retirement Services, Michigan Unemployment Services, Minnesota Unemployment Services, Mississippi Unemployment Services, Missouri State Employees,Missouri Unemployment Services, Montana State Employees,Montana TRS, Montana Unemployment ServicesMOSERS, MPERA, MSRS, MyEPP, National Capital Planning Commission, Navy Exchange Service Command, Navy Federal Credit Union, NDPERS, Nebraska Unemployment Services, Nevada State Employees, Nevada Unemployment Services, New Hampshire Unemployment Services, New Jersey State Employees, New Jersey Unemployment Services, New Mexico ERB, New Mexico Unemployment Services, New York State Employees, New York Unemployment Services, NHRS, NJTPAF, North Carolina Retirement Systems, North Carolina State Employees, North Carolina Unemployment Services, North Dakota TFFR, North Dakota Unemployment Services, NPERS, NSERS, NVPERS, NYC Child Support, NYC Employee Retirement System, NYSLRS, NYSTRS, Ohio State Employees, Ohio Unemployment Services, OhioPERS, Oklahoma Unemployment Services, OPERS, Oregon PERS, Oregon Unemployment Services, Peace Corps, Pearl Harbor Naval Shipyard, Pennsylvania SERS, Pennsylvania State Employees, Pennsylvania Unemployment Services, Pentagon Force Protection Agency, PERA of New Mexico, PERS of Mississippi, PERSI, PSERS, PSRS Missouri, Rhode Island State Employees, Rhode Island Unemployment Services, Robins Air Force Base, SCRS, SERS Ohio, Small Business Administration, Smithsonian Institution,Social Security, South Carolina State Employees, South Carolina Unemployment Services, South Dakota Unemployment Services, SSI, Steelworkers Pension Trust, STRS Ohio, Teachers Retirement System, Teachers Retirement System of Alabama, Tennessee CRS, Tennessee Unemployment Services, Texas Unemployment Services, The Retirement Systems of Alabama, Transportation Security Administration, Treasury Technical Assistance, TRS Illinois, TRS of Kentucky, TRS of Texas, TRSGA, TRSL, U.S. Agency for International Development, U.S. Capitol Police, US Air Force, US Air Force Reserves, US Army, US Army Corps of Engineers, US Army Reserve, US Coast Guard, US Department of Agriculture, US Department of Commerce, US Department of Defense, US Department of Energy, US Department of Health and Human Services, US Department of Homeland Security, US Department of Justice, US Department of Labor, US Department of Treasury, US Forest Service, US Marine Corps, US Navy, US Office of Personnel Management, US Space Force, US Veterans Affairs, Utah Retirement Systems, Utah Unemployment Services, Vermont Unemployment Services, Veteran's Benefits, Veterans Benefits, Veterans Education Benefits, Virginia Retirement System, Virginia State Employees, Virginia Unemployment Services, VSERS, Washington State Department of Retirement Systems, Washington State Employees, Washington Unemployment Services, West Virginia PERS, West Virginia State Employees, West Virginia Unemployment Services, Wisconsin EFT, Wisconsin Unemployment Services,WVTRS, Wyoming Retirement System, Wyoming Unemployment Services
```

```
Q: What is the token property in the create Atomic access token API (POST /access-token) response? We've noticed that the docs only reference the publicToken and not the token we seem to also be getting back.
A: You can safely ignore the token property. It is currently deprecated, but not yet fully sunset. publicToken was released a while back to replace it, so you are using the correct field.

Q: When is a Linked Account created? Is this created when we create an access token for a user with a given "identifier"? Or, when a user performs a successful login with their payroll provider via the Atomic Transact SDK? Or, when a user has successfully setup a direct deposit via the Atomic Transact SDK? Or, is it something else?
A: The Linked Account is created after the user has successfully authenticated with the payroll system.

Q: Since a Linked Account is a "persistent connection that has been authenticated by an end-user", when this connection expires, what needs to be done to re-establish the connection? (Asking here because this will depend on the answer to 2a).
A: When the connection for a Linked Account is lost (password changed, etc.) we send out the linked-account-disconnected webhook. This will require the user to reauthenticate through Transact. You can use the linkedAccount._id when initializing Transact to start the flow at the authentication page for that user. You put that value in the linkedAccount parameter of the Transact config.

Q: Will we only receive webhook events related to direct deposits setup via the Atomic Transact SDK, or will this include all activity that occurs at the payroll provider as it relates to the user?
A: You will receive monitoring events based on the state of the payroll system. So any Deposit Accounts whether set up through Atomic or not will be returned in the Deposit Accounts webhooks. Any other data will depend on what you have configured in the Monitoring section of the Features page in Console.

Q: Regarding the task-status-updated webhook event, does a status = "completed" mean the direct deposit has been successfully setup with the payroll provider? If so, how is this different from the deposit-account-added webhook event?
A: Yes, you are correct. status: completed indicates a successful direct deposit allocation. They are similar, but deposit-account-added is sent out due to an update on the payroll system side. So, if you are monitoring a payroll system and the user adds another account to their payroll system either directly or via other means, when we next detect this change in the state of the system, we send out the deposit-account-added webhook. Think of this webhook more as a monitoring webhook for changes on the payroll system vs task-status-updated with a completed status being the webhook sent out when an Atomic task to add or update a deposit account on the payroll system has resolved.

Q: Is it possible to remove a payroll allocation via Atomic?
A: The only way we currently have to remove a payroll allocation is for a user to go through Transact and set the deposit amount to 0.
```

```
Q: We're referring to the case when user has 2 jobs, hence 2 providers issue payroll to this user, and user wants to connect both to Revolut bank account one by one. Can they use the same token to issue the second payroll?
A: the token is time based ... so if they are doing it back to back and it hasn't expired, then they can just pass the same token. Once the token expires, if the user comes back to link their second job they will need to regenerate a token. i.e. they can use that same token for the same user multiple times within the expiration timeframe. Each time the user goes through will generate a new task with new task ids , connector ids, etc.
```