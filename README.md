# A Case of the Mondays  
<p align="center">
  <img src="https://media-exp1.licdn.com/dms/image/C4E12AQH5QLP7UTNQrg/article-cover_image-shrink_600_2000/0?e=1610582400&v=beta&t=vnmUJFfaFbU1DjFrfGe6JWXFQ5c38DTif6D-bUEHL4E">
</p>  

## About The Project
As an employee at Initech, I've got a bad case of the *Mondays*. Could you do me a favor? The worst that could happen is we get put into a white-collar, minimum-security resort (I heard they have conjugal visits). Pinky promise!  
### Background
<p align="center">
  <img src="https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/052013/initech-edited-colors-font-vectorized.png?itok=IQhihDgr">
</p>  

My friends and I work at [Initech](https://movies.stackexchange.com/questions/726/what-kind-of-company-is-initech) - a software consulting company for banks. They hire computer programmers to update software for the dreaded Y2k switch.
### Goals
We wanted to collect the leftover penny fractionals when calculating interest is rounded - and deposit these into a seperate bank acount. But things didn't go as planned. Rather than skimming fractions of a cent per transaction, more than $300,000 appeared in the account in one day.   
My friend Michael Bolton says...   
> "I must have put a decimal point in the wrong place or something.
> I always do that. I always mess up some mundane detail."  

We need your help to figure out what went wrong, and fix it *asap*.
### Data Dictionary
| Column              | Description                                               | Data Type  |
|---------------------|-----------------------------------------------------------|------------|
| balance             | total amount in bank $                                    | random     |
| interest_rate       | the rate account earns interest                           | random     |
| calculated_interest | a percentage of balance, based on interest rate           | calculated |
| new_balance         | original balance + interest earned  (calculated interest) | calculated |  

## Project Steps
### Put the New [Coversheet](https://en.wikipedia.org/wiki/TPS_report) on that TPS Report
"We're putting new coversheets on all the TPS reports before they go out now. So if you could go ahead and try to remember to do that from now on, that'd be great."  
In case you didn't get the memo.  

![TPS-Report](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Tps_report.png/440px-Tps_report.png)
### Attend a Hypnotherapy Session
According to [VeryWellMind.com](https://www.verywellmind.com/hypnotherapy-2671993),
> "Hypnotherapy is a form of adjunctive technique that utilizes hypnosis to aid in the treatment of different specific symptoms or conditions...Although results 
> tend to be controversial, many experts believe that hypnotherapy works in some cases."
### Acquire the data
Using numpy random number generators, a data frame of fake bank data is created. The data frame includes:
- total balance in the account
- interest rate
- earned interest
- new balance after adding earned interest  

I've included the notebook which walks through the process of creating this df. The Data.py module contains this process in one function. You only need to download Data.py to generate the dataframe. However, if you want to tweak the data, feel free to do so in the notebook and add these changes to your Data.py file. I suggest making changes in the notebook first to make the process easier.
### Fix the Bug
We've already created the "virus". Now we need your help to fix the bug. The function was *supposed* to take the leftover interest after being rounded. It should have been amounts less than a penny.  

As Peter Gibbons explains it,  
> "When the sub routine compounds the interest it uses all these extra decimal places that just get rounded off. So we simplified the whole thing, we rounded 
> them all down, drop the remainder into an account we opened...Like the 7-11. You take a penny from the tray, right? Well those are whole pennies, right? I'm just 
> talking about fractions of a penny here. But we do it from a much bigger tray and we do it a couple a million times."  

## Conclusion
Don't learn the hard way. Test your code before it's too late!
## How to Reproduce

<p align="center">
  <img src="https://thumbs.gfycat.com/GroundedSophisticatedFieldmouse-size_restricted.gif">
</p> 

- [x] Read this Readme.md
- [ ] Download Data.py, Floppy_Disk.py, Bank_Statement.py, and Debugging.ipynb into your working directory (no floppy disks needed)
- [ ] Fix the function in Floppy_disk.py to correctly run each transaction.
    - If you get stuck, check out Solution.ipynb also available to view or download, this holds the correct function
- [ ] Determine if your fix will go undetected by corporate. What's the balance?
    - Work in the Debugging notebook or create your own notebook
    - Use the function in Bank_Statement.py called deposits()
    - Set the transactions parameter to your own liking, this is how many times an account is rounded down and we skim the change
    - Is it depositing pennies at a time like it should?
- [ ] ~~Set the building on fire~~
## Next Steps
Now that the bug is outta the way, let's focus on the more important issue... How to calculate the perfect person-to-cake ratio?  

<p align="center">
  <img src="https://www.teamphoria.com/wp-content/uploads/9imQZkq.jpg">
</p> 

# Author
![Name-Tag](https://i.pinimg.com/originals/e1/56/2b/e1562bc3f546913c96df7903f57fdeb2.png)  

Hope you have as much fun with this as I did making it!
Feel free to reach out to me at thompson.bethany.01@gmail.com with any questions, suggestions, or more!
Oh, and if you could just turn that TSP coversheet in, that'd be greaaat.
