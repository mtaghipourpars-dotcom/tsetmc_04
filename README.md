# TSETMC 04 — Iran Trading System

سامانه تصمیم‌یار و تحقیقاتی بازار سرمایه ایران. این مخزن از مجموعه ۶۰ مشخصات مستقل Skill و مستندات پایه معماری تشکیل شده است.

> **وضعیت فعلی: SPECIFICATION / DESIGN BASELINE.** این مخزن هنوز کد اجرایی، اتصال زنده TSETMC، API کارگزاری، موتور سفارش یا داشبورد عملیاتی ارائه نمی‌کند.

## شروع از کجا؟
- [کاتالوگ مادر ۶۰ Skill](MASTER_CATALOG.md)
- [مشخصات Skillها](skills/)
- [معماری کلان](docs/ARCHITECTURE.md)
- [قراردادهای داده](docs/DATA_CONTRACTS.md)
- [امنیت و حاکمیت](docs/SECURITY_AND_GOVERNANCE.md)
- [وضعیت پیاده‌سازی](docs/IMPLEMENTATION_STATUS.md)
- [نقشه راه](docs/ROADMAP.md)
- [راهنمای توسعه](docs/DEVELOPMENT_GUIDE.md)

## ساختار
- skills/: 60 فایل مستقل SKILL-01.md تا SKILL-60.md
- docs/: معماری، قرارداد داده، امنیت، وضعیت و نقشه راه
- MASTER_CATALOG.md: فهرست مادر
- .env.example: نمونه تنظیمات بدون secret

## مرزبندی داده
هر داده باید یکی از کلاس‌های LIVE، HISTORICAL، SIMULATED، DEMO یا ASSUMPTION داشته باشد. LIVE تنها با اتصال تأییدشده و کنترل تازگی مجاز است.

## ایمنی معاملات
هیچ Skill به‌تنهایی مجاز به ارسال سفارش واقعی نیست. هرگونه اتصال کارگزاری و اجرای سفارش در فاز جداگانه، پس از تست sandbox، کنترل ریسک، احراز هویت، audit و تأیید انسانی صریح قابل بررسی است.

## زبان و منطقه
مستندات فارسی/انگلیسی هستند. زمان، واحد پول، تقویم معاملاتی و تبدیل تاریخ باید صریح و قابل ردیابی باشند.

## مشارکت
راهنمای [CONTRIBUTING.md](CONTRIBUTING.md) را ببینید.
