# قراردادهای داده

## کلاس داده
| برچسب | معنی |
|---|---|
| LIVE | داده زنده از منبع متصل و سالم؛ فقط با اثبات تازگی |
| HISTORICAL | داده تاریخی منبع‌دار |
| SIMULATED | خروجی مدل یا شبیه‌سازی |
| DEMO | داده نمایشی یا ساختگی |
| ASSUMPTION | فرض صریح کاربر یا تحلیلگر |

## Metadata حداقلی
source_id، instrument_id، event_time، ingested_at، timezone، currency، unit، data_class، schema_version، raw_ref و quality_status.

زمان رویداد با زمان دریافت متفاوت است و هر دو باید نگهداری شوند. تاریخ شمسی در UI مجاز است؛ ذخیره‌سازی canonical باید قابل مقایسه باشد. قیمت خام هرگز overwrite نشود؛ قیمت تعدیل‌شده به روش، رویداد، ضریب و نسخه الگوریتم ارجاع دهد.

وضعیت کیفیت: VALID، SUSPECT، STALE، MISSING، CONFLICTED و REJECTED. پاک‌سازی خاموش مجاز نیست.
