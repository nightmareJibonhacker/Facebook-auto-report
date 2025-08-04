import time
import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 Chrome/112.0.5615.138 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Linux; U; Android 10; en-US; SM-A107F) AppleWebKit/537.36 Chrome/99.0.4844.94 Mobile Safari/537.36"
]

def ask_facebook_id():
    fb_id = input("Report করতে চান, সেই Facebook ID/Link দিন: ")
    return fb_id

def ask_report_count():
    while True:
        try:
            count = int(input("কত রিপোর্ট করতে চান? সংখ্যা লিখুন: "))
            if count > 0:
                return count
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

def send_report(fb_id, reason, number):
    user_agent = random.choice(USER_AGENTS)
    print(f"Report #{number+1}:")
    print(f"  Target Facebook ID/Link: {fb_id}")
    print(f"  Reason: {reason}")
    print(f"  User-Agent: {user_agent}")
    # এখানে আসল Facebook API/reporting endpoint থাকলে, HTTP request পাঠানো যেত
    time.sleep(1)  # Simulate network delay

def main():
    fb_id = ask_facebook_id()
    count = ask_report_count()
    reason = "Unethical activity / spam / abuse"
    print(f"\n{fb_id} আইডিতে মোট {count} বার রিপোর্ট পাঠানো হবে।\n")
    for i in range(count):
        send_report(fb_id, reason, i)
    print(f"\nFinished! {fb_id} আইডিতে {count} টি রিপোর্ট (সিমুলেটেড) পাঠানো হয়েছে।\n")

if __name__ == "__main__":
    main()
