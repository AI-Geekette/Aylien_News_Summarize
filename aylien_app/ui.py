import gradio as gr
import pandas as pd

# Function to generate the news content and summaries
def generate_news_data(word):
    # Here, you would have your own logic to fetch and process news data based on the provided word

    # Sample data for demonstration
    news_content = [
        "We and our partners store and/or access information on a device such as unique IDs in cookies to process personal data. You may accept or manage your choices by clicking below including your right to object where legitimate interest is used or at any time in the privacy policy page. These choices will be signaled to our partners and will not affect browsing data.The burn rate of the meme-inspired cryptocurrency Shiba Inu ($SHIB) has recently surged by more than 8000% as millions of tokens are moved to inaccessible wallets and effectively removed from circulation. According to SHIB burn tracking platform Shibburn over the last 24-hour period a total of 50.18 million tokens were burned. The figure came through only two transactions that show large holders were burning tokens rather than coming from several individual entities. The burn was made via two burns one for 39511911 SHIB and another for 10676779 SHIB. Cumulatively the efforts of the SHIB community have resulted in the burn of 3093934362 SHIB coins in the past week. Since the meme-inspired cryptocurrency was launched around 410.63 trillion tokens have been destroyed from a total supply of 1 quadrillion. As CryptoGlobe reported the recently launched Koyo token project has moved forward with a major burn of the meme-inspired cryptocurrency last month destroying an astounding 1.49 billion tokens in a single transaction. Powered By 10 Bitcoin Outlook as Trading Range Narrows to Tightest in Months Share Next Stay Shytoshi Kusama SHIB\u2019s lead developer recently shared his thoughts on the relationship between Shiba Inu\u2019s price and burns in a telegram chat. According to Kusama the price of Shiba Inu cannot be influenced solely by burns and more burns are needed to move its price. Recently the Shiba Inu team has unveiled the intricacies of the SHIB burn mechanism on the Shibarium Layer 2 network which currently operates in beta test mode. For every transaction that occurs on Shibarium a fee in $BONE is levied. This fee is locked in a contract with the team receiving 30% of it for network maintenance and 70% being burned. Recently shared screenshots indicate that the fee can be burned only when the contract contains more than 10 BONE. Then the tokens can be converted into SHIB and burned As CryptoGlobe reported a newly formed mysterious SHIB wallet has recently accumulated a whopping 20 trillion tokens for around $176.8 million making it the fifth-largest holder of the meme-inspired cryptocurrency. The investor now holds around 2% of the cryptocurrency\u2019s supply. Image Credit Featured Image via Unsplash Shiba Inu ($SHIB) Burn Rate Skyrockets by 8000% as Shibarium Unveils Burn Mechanism /latest/2023/05/shiba-inu-shib-burn-rate-skyrockets-by-8000-as-shibarium-unveils-burn-mechanism/ /latest/2023/05/xrp-security-or-not-a-security-that-is-the-question-insights-from-a-prominent-attorney/ Disclaimer The views and opinions expressed by the author or any people mentioned in this article are for informational purposes only and they do not constitute financial investment or other advice. Investing in or trading cryptoassets comes with a risk of financial loss. Related Articles Jesse Hynes a prominent American lawyer provides his expert perspective on the SEC\u2019s ongoing lawsuit against Ripple Labs and the future of XRP. Hynes an established American attorney and Chief Legal Officer at Gala Games recently took to Twitter to weigh in on the ongoing lawsuit against Ripple Labs initiated by the U.S. Securities and Exchange Commission (SEC) in December 2020. This case centers around allegations of illegal sales of XRP tokens which the SEC tends to regard as security much like most other crypto tokens. On May 22 2023 Hynes posted a series of tweets sharing his predictions about the potential verdicts of the case. Beginning with the consideration of XRP\u2019s early-day sales he postulated that they might be deemed as violations of securities laws. This decision he believes could pave the way for the SEC to take similar action against numerous other firms engaged in fundraising via sales which according to his interpretation equates to the creation of an investment contract. Despite these alleged early infringements Hynes expressed a belief that Ripple\u2019s current sales practices could be adjudged as compliant with securities laws by the court. In his view a key issue is whether XRP itself falls within the definition of a security especially given its history of sales that may be characterized as securities. Hynes also raised concerns that the court may refrain from addressing this pivotal question which in his estimation could complicate the case resolution. However he also recognized that the SEC\u2019s recent actions and claims could potentially influence the court to reach a decision on this matter. If this were to happen Hynes indicated that he would view the SEC\u2019s insistence on this point as instrumental in compelling the court to provide clarity. When contemplating the court\u2019s stance on XRP\u2019s status moving forward Hynes held a 50/50 view on whether the court would make a determination. If the court were to delve into this issue he argued that the only rational conclusion would be that XRP does not fit the mold of an investment contract. He further speculated that Ripple\u2019s fair notice defense could become relevant if the court unexpectedly determined that XRP as an asset is an investment contract. In such a scenario Ripple could legitimately claim that it was not given adequate warning of this interpretation. However Hynes quickly clarified that this defense would likely be advantageous to Ripple rather than its user base. Despite the various potential outcomes of the case Hynes consistently maintained his doubt that the court would conclude that the XRP asset is a security. XRP: Security or Not a Security That Is the Question: Insights from a Prominent Attorney /latest/2023/05/xrp-security-or-not-a-security-that-is-the-question-insights-from-a-prominent-attorney/ /latest/2023/05/the-great-crypto-and-tech-rally-a-former-wall-street-insider-predicts-the-future/"
    ]
    news_summaries = [
        " The burn rate of the meme-inspired cryptocurrency Shiba Inu ($SHIB) has recently surged by more than 8000%. This was achieved through two transactions that show large holders burning tokens rather than coming from several individual entities. This has resulted in the burn of 3093934362 SHIB coins in the past week. Jesse Hynes, an American lawyer and Chief Legal Officer at Gala Games, recently shared his thoughts on the SEC\u2019s ongoing lawsuit against Ripple Labs. He postulated that early sales of XRP might be deemed as violations of securities laws, but he believes current sales practices could be adjudged as compliant with securities laws. He expressed a belief that the only rational conclusion would be that XRP does not fit the mold of an investment contract, however, he is unsure if the court will make a determination."
    ]

    # Creating a pandas DataFrame for the news content and summaries
    df = pd.DataFrame({"Original News": news_content, "News Summaries": news_summaries})

    return df

# Creating the Gradio interface
def gradio_interface():
    # Input component: Textbox for entering a word
    word_input = gr.inputs.Textbox(label="Enter a word")

    # Output component: HTML to display two columns of data with hover effect
    news_output = gr.outputs.HTML(label="")

    # Function to be called when the interface is used
    def summarize_news(word):
        df = generate_news_data(word)

        # Wrap the truncated text in a span with a title attribute for hover effect
        def wrap_text(text):
            truncated_text = text[:100] + "..." if len(text) > 100 else text
            return f'<span title="{text}">{truncated_text}</span>'

        # Apply the wrap_text function to each cell in the DataFrame
        df = df.applymap(wrap_text)

        # Generate HTML table with two columns
        html_table = df.to_html(classes="table table-striped", index=False, escape=False)

        # Wrap the table in a div to control the width
        html_output = f'<div style="width: 100%;">{html_table}</div>'
        return html_output

    # Create Gradio Interface
    interface = gr.Interface(fn=summarize_news, inputs=word_input, outputs=news_output, title="News Summarizer")

    return interface

# Running the interface
if __name__ == "__main__":
    interface = gradio_interface()
    interface.launch()
