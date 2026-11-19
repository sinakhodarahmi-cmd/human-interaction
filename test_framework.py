import openai
from main import SentimentAwareAI # فرض می‌کنیم کد قبلی را در main.py ذخیره کرده‌ای

class ProjectEvaluator:
    def __init__(self, api_key):
        self.agent = SentimentAwareAI(api_key)
        # تعریف سناریوهای تست برای ارزیابی دقت سیستم
        self.test_scenarios = [
            {"input": "I am so happy today! Everything is perfect!", "expected_mood": "positive"},
            {"input": "This is terrible. I am extremely frustrated and angry.", "expected_mood": "negative"},
            {"input": "The weather is cloudy and the temperature is 20 degrees.", "expected_mood": "neutral"},
            {"input": "I feel so lonely and sad right now...", "expected_mood": "negative"},
            {"input": "That's a great idea, let's do it!", "expected_mood": "positive"}
        ]

    def run_evaluation(self):
        print("🚀 Starting Automated Evaluation Suite...\n")
        print(f"{'Input Text':<50} | {'Expected':<10} | {'Result'}")
        print("-" * 80)

        success_count = 0

        for scenario in self.test_scenarios:
            user_text = scenario["input"]
            expected = scenario["expected_mood"]
            
            # در اینجا ما مستقیماً از متد داخلی برای تست دقت استفاده می‌کنیم
            # (برای تست دقیق‌تر، باید متد _analyze_sentiment را در دسترس قرار دهیم)
            mood, score = self.agent._analyze_sentiment(user_text)
            
            # بررسی صحت تشخیص
            is_correct = (mood == expected)
            if is_correct:
                success_count += 1
            
            status = "✅ PASS" if is_correct else "❌ FAIL"
            
            print(f"{user_text[:48]:<50} | {expected:<10} | {status} (Detected: {mood})")

        # محاسبه دقت نهایی (Accuracy)
        accuracy = (success_count / len(self.test_scenarios)) * 100
        print("-" * 80)
        print(f"📊 Final Accuracy Score: {accuracy:.2f}%")
        print(f"📈 Status: {'Ready for Research Publication' if accuracy > 80 else 'Needs Refinement'}")

if __name__ == "__main__":
    # جایگذاری کلید خودت
    MY_API_KEY = "your-api-key-here" 
    
    evaluator = ProjectEvaluator(MY_API_KEY)
    evaluator.run_evaluation()
