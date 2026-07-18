# المكدس التقني ونوع الحل

## الغرض

توثق هذه الوثيقة نوع الحل والمكدس التقني والمعماريات الهندسية والقيود التنفيذية المعتمدة لمنصة إدارة المشاريع المؤسسية لصندوق البيئة.

تعد هذه الوثيقة مرجع القرار التقني الأعلى للمشروع، ولا تستبدل وثائق المعمارية التفصيلية أو تصميم البيانات أو التكامل أو الأمن أو التشغيل أو تجربة المستخدم. يجب أن تتوافق تلك الوثائق مع القرارات الواردة هنا، وأي استثناء يتطلب قرارًا معماريًا موثقًا.

## معلومات الوثيقة

| الحقل | القيمة |
|---|---|
| المشروع | منصة إدارة المشاريع المؤسسية لصندوق البيئة |
| الاسم الإنجليزي | Environment Fund Enterprise Project Management Platform |
| نوع الوثيقة | Technology Stack and Solution Type |
| مالك الوثيقة | TBD — يحدد من صندوق البيئة |
| أُعدت بواسطة | تحليل نظم ومعمارية حلول بمساعدة الذكاء الاصطناعي وتحت توجيه المستخدم |
| المراجعون | TBD — معمارية المؤسسة والأمن السيبراني والتطبيقات والبيانات والتكامل والتشغيل والجودة |
| الإصدار | 0.2 |
| الحالة | Draft |
| التصنيف | Internal |
| آخر تحديث | 2026-07-18 |

## السياق المطلوب

1. `docs/00-Project-Index.md`
2. `docs/01-Requirements/01-Project-Overview.md`
3. `docs/01-Requirements/02-Business-Requirements.md`
4. `docs/01-Requirements/03-System-Requirements.md`
5. `docs/01-Requirements/04-Delivery-Backlog.md`
6. `docs/01-Requirements/05-Traceability-Matrix.md`

## 1. ملخص القرار التقني

يعتمد المشروع حلًا مطورًا خصيصًا وفق القرارات التالية:

| المجال | القرار المعتمد | الحالة |
|---|---|---|
| نوع الحل | تطبيق ويب مؤسسي مطور خصيصًا | Confirmed |
| النمط العام | Modular Monolith | Confirmed |
| معمارية الخادم | Business Modules مع Vertical Slices داخل كل وحدة | Confirmed |
| تنظيم الواجهة | Feature-based architecture متوافقة مع وحدات الأعمال | Confirmed |
| الواجهة الأمامية | React 19.2.7 مع TypeScript 6.0 | Confirmed |
| أداة البناء | Vite 8.1 | Confirmed |
| التوجيه | React Router 8.2 | Confirmed |
| التنسيق البصري | Tailwind CSS 4.3 باستخدام إضافة Vite الرسمية | Confirmed |
| Backend | ASP.NET Core على .NET 10.0.10 LTS | Confirmed |
| لغة الخادم | C# 14 | Confirmed |
| الوصول للبيانات | Entity Framework Core 10.0.10 | Confirmed |
| قاعدة البيانات | SQL Server 2025 | Confirmed |
| نمط API | Minimal APIs وRoute Groups وTyped Results | Confirmed |
| أسلوب الأوامر والاستعلامات | CQRS-lite دون فرض MediatR | Confirmed |
| الهوية | Microsoft Entra ID للـSSO | Confirmed |
| ERP | Oracle Fusion Cloud ERP | Confirmed |
| البريد والتقويم | Microsoft Exchange عبر Microsoft Graph | Confirmed |
| اللغات | العربية RTL والإنجليزية LTR | Confirmed |
| الاستضافة | TBD — تتطلب قرارًا معماريًا وتشغيليًا وأمنيًا | Open |

## 2. خط أساس الإصدارات

### 2.1 الإصدارات الأساسية المعتمدة

الإصدارات التالية هي خط أساس التوثيق بتاريخ 2026-07-18:

| المكون | الإصدار الأساسي | سياسة الاستخدام |
|---|---:|---|
| React | 19.2.7 | أحدث إصدار ثابت ضمن React 19.2 وقت التوثيق |
| React DOM | 19.2.7 | يجب أن يطابق إصدار React |
| React Router | 8.2 | أحدث إصدار ثابت موثق وقت التوثيق |
| React Compiler | 1.x stable | يفعّل تدريجيًا بعد اجتياز فحوص Rules of React |
| TypeScript | 6.0 | إصدار ثابت؛ لا يستخدم TypeScript 7 Preview في الإنتاج |
| Vite | 8.1 | الإصدار المدعوم الحالي مع Rolldown |
| Tailwind CSS | 4.3 | يستخدم من خلال `@tailwindcss/vite` |
| Node.js | 24.18 LTS | يستخدم للبناء والتطوير وCI؛ لا يستخدم Node 26 Current للإنتاج |
| .NET Runtime | 10.0.10 LTS | آخر Patch أمني وقت التوثيق |
| .NET SDK | 10.0.302 | مثبت في `global.json` مع سياسة Roll Forward محكومة |
| ASP.NET Core | 10.0.10 | ضمن Runtime .NET 10 المتوافق |
| Entity Framework Core | 10.0.10 | توحد جميع حزم EF Core على Patch واحد |
| C# | 14 | وفق .NET 10 SDK |
| SQL Server | SQL Server 2025 | يستخدم آخر CU وGDR معتمدين في البيئة |
| SQL Server build baseline | 17.0.4060.2 | CU6 + GDR بتاريخ 2026-07-14؛ يحدث أمنيًا قبل النشر |

### 2.2 سياسة الإصدارات والتحديث

- يمنع استخدام إصدارات Preview أو Beta أو RC أو Canary في الإنتاج.
- تثبت الإصدارات المباشرة في ملفات المشروع وملف القفل، ولا يعتمد النطاق `latest` في بناء قابل للإصدار.
- تستخدم أحدث Patch أمني متوافق عند إنشاء البيئة أو الإصدار، بعد اجتياز الاختبارات الآلية والرجعية.
- يتطلب الانتقال إلى Major جديد قرارًا معماريًا وخطة ترقية واختبار توافق ورجوع.
- تثبت نسخة Node.js في ملف `.nvmrc` أو `.node-version` وفي إعداد CI.
- تثبت نسخة .NET SDK في `global.json`.
- تدار حزم .NET مركزيًا باستخدام `Directory.Packages.props`.
- يستخدم ملف قفل واحد معتمد لحزم الواجهة، ويفضل `pnpm-lock.yaml`.
- تفحص الحزم دوريًا للثغرات والتراخيص والصيانة والتبعيات المتروكة.
- لا تضاف مكتبة خارجية عندما تكفي قدرات المنصة أو المتصفح أو .NET بصورة واضحة وقابلة للصيانة.

## 3. نوع الحل والنمط المعماري

### 3.1 نوع الحل

| الحقل | القرار |
|---|---|
| Primary Solution Type | Custom Enterprise Web Application |
| Application Shape | React SPA + ASP.NET Core API + SQL Server |
| Backend Architecture | Modular Monolith |
| Internal Structure | Business Modules containing Vertical Slices |
| Delivery Model | TBD — داخلي أو مشترك أو من خلال مورد |
| Hosting Model | TBD |
| Integration Boundary | Oracle Fusion Cloud ERP وMicrosoft Entra ID وMicrosoft Exchange فقط |

### 3.2 لماذا Modular Monolith

يعتمد Modular Monolith لأنه يوفر:

- حدودًا واضحة بين مجالات الأعمال دون تكلفة التشغيل الموزع المبكرة؛
- نشرًا وتشغيلًا ومراقبة أبسط من Microservices؛
- معاملات بيانات موثوقة داخل النظام؛
- إمكانية فصل وحدة إلى خدمة مستقلة مستقبلًا عند وجود مبرر تشغيلي مثبت؛
- سهولة الحفاظ على التتبع والتدقيق والاتساق في نظام مؤسسي مترابط؛
- تقليل التعقيد في الشبكات والمراسلة والاتساق النهائي وإدارة الإصدارات الموزعة.

لا يجوز تحويل الحل إلى Microservices لمجرد الفصل التنظيمي. يتطلب الفصل المستقبلي أدلة على الحاجة إلى استقلال النشر أو التوسع أو الملكية أو العزل أو دورة الحياة.

### 3.3 المبادئ الملزمة للوحدات

- تمثل الوحدة مجال أعمال متماسكًا وليس طبقة تقنية.
- تملك كل وحدة نموذجها ومنطقها وواجهاتها الداخلية وتهيئتها وتخطيطها البياني.
- يمنع الوصول المباشر من وحدة إلى جداول أو `DbContext` وحدة أخرى.
- يتم التواصل عبر عقود داخلية واضحة أو أحداث داخلية أو Read Models مصرح بها.
- يبقى Shared Kernel صغيرًا ولا يتحول إلى مستودع مشترك لكل شيء.
- يمنع إنشاء مشروع عام باسم `Common` أو `Helpers` لتجميع منطق غير مصنف.
- توثق التبعيات المسموحة بين الوحدات وتختبر آليًا بواسطة Architecture Tests.

## 4. معمارية Backend

### 4.1 البنية المقترحة

```text
src/
├── Eppm.Api/
│   ├── Authentication/
│   ├── Authorization/
│   ├── Middleware/
│   ├── OpenApi/
│   ├── HealthChecks/
│   └── Program.cs
├── Eppm.Modules/
│   ├── Strategy/
│   ├── DemandManagement/
│   ├── PortfolioManagement/
│   ├── ProgramManagement/
│   ├── ProjectManagement/
│   ├── WorkManagement/
│   ├── ResourceManagement/
│   ├── FinancialManagement/
│   ├── ProcurementAndContracts/
│   ├── DeliverablesAndQuality/
│   ├── RiskAndIssues/
│   ├── ChangeControl/
│   ├── GovernanceAndMeetings/
│   ├── BenefitsManagement/
│   ├── Reporting/
│   └── Administration/
├── Eppm.Integrations/
│   ├── OracleFusion/
│   ├── MicrosoftEntra/
│   └── MicrosoftExchange/
├── Eppm.SharedKernel/
│   ├── Primitives/
│   ├── Auditing/
│   ├── Authorization/
│   ├── Errors/
│   └── Messaging/
├── Eppm.ServiceDefaults/
└── Eppm.AppHost/
```

### 4.2 Vertical Slice Architecture

ينظم كل استخدام أعمال في Slice مستقلة:

```text
ProjectManagement/
└── Features/
    ├── CreateProject/
    │   ├── Endpoint.cs
    │   ├── Request.cs
    │   ├── Response.cs
    │   ├── Validator.cs
    │   ├── Handler.cs
    │   ├── Authorization.cs
    │   ├── Mapping.cs
    │   └── Tests.cs
    ├── UpdateProject/
    ├── SubmitProjectForApproval/
    ├── GetProjectDetails/
    └── CloseProject/
```

يكون تدفق الطلب الأساسي:

```text
HTTP Request
→ Authentication
→ Authorization
→ Validation
→ Handler
→ Domain Rules
→ EF Core / Integration Adapter
→ Transaction and Outbox
→ Typed Response
```

### 4.3 قرارات التنفيذ

- تستخدم Minimal APIs مع Route Groups حسب الوحدة أو Feature.
- تستخدم `TypedResults` لضمان عقود استجابة واضحة.
- يستخدم RFC Problem Details للأخطاء.
- يعتمد OpenAPI الرسمي في ASP.NET Core لتوليد عقد API.
- تستخدم Commands للتغييرات وQueries للقراءة ضمن CQRS-lite.
- يستدعي Endpoint الـHandler مباشرة من Dependency Injection.
- لا يعد MediatR اعتمادًا إلزاميًا، وأي استخدام له يتطلب مراجعة الترخيص والقيمة الفعلية.
- لا يستخدم Generic Repository فوق EF Core.
- لا ينشأ Unit of Work wrapper عام فوق `DbContext`.
- لا تعاد Entities مباشرة إلى الواجهة؛ تستخدم Request وResponse DTOs.
- تستخدم Cancellation Tokens في جميع العمليات غير الفورية.
- تستخدم Async APIs دون حجب Threads.
- تطبق Optimistic Concurrency على السجلات التي تتعرض لتعديل متزامن.

### 4.4 البيانات والمعاملات

- تستخدم قاعدة SQL Server واحدة مبدئيًا مع Schema مستقل لكل وحدة.
- يفضل `DbContext` مستقل لكل وحدة عندما يخدم حدود الملكية بوضوح.
- لا يسمح بإنشاء Foreign Keys عابرة للوحدات دون قرار تصميم مبرر.
- تستخدم معرفات ثابتة وغير قابلة لإعادة الاستخدام.
- تحفظ أوقات النظام بصيغة UTC ويطبق العرض المحلي في الواجهة.
- تحفظ سجلات التدقيق والتغييرات والاعتمادات وفق تصميم أمني وسجلاتي مستقل.
- تطبق Transactional Outbox للأحداث والتكاملات التي يجب ألا تضيع.
- تطبق Idempotency على الطلبات والتكاملات القابلة للتكرار.

## 5. معمارية React الحديثة

### 5.1 نمط التطبيق

الواجهة تطبيق مؤسسي Client-side SPA يتصل بـASP.NET Core API. لا يعتمد SSR أو React Server Components ضمن خط الأساس الحالي، لأن المشروع يعتمد Backend مستقلًا في .NET ولا توجد حاجة موثقة حاليًا لمحركات بحث عامة أو Rendering على الخادم.

أي إدخال لـSSR أو React Server Components يتطلب قرارًا معماريًا مستقلًا وتحليل أمن وتشغيل وتكلفة، ولا يستخدم بصورة افتراضية.

### 5.2 البنية المقترحة

```text
web/
├── src/
│   ├── app/
│   │   ├── bootstrap/
│   │   ├── providers/
│   │   ├── router/
│   │   ├── layouts/
│   │   ├── auth/
│   │   └── configuration/
│   ├── modules/
│   │   ├── projects/
│   │   │   ├── features/
│   │   │   │   ├── create-project/
│   │   │   │   ├── edit-project/
│   │   │   │   ├── submit-project/
│   │   │   │   └── close-project/
│   │   │   ├── pages/
│   │   │   ├── components/
│   │   │   ├── api/
│   │   │   ├── schemas/
│   │   │   ├── hooks/
│   │   │   ├── types/
│   │   │   └── tests/
│   │   ├── portfolios/
│   │   ├── programs/
│   │   ├── resources/
│   │   ├── finance/
│   │   ├── contracts/
│   │   ├── risks/
│   │   └── administration/
│   ├── shared/
│   │   ├── ui/
│   │   ├── api/
│   │   ├── hooks/
│   │   ├── localization/
│   │   ├── validation/
│   │   ├── utilities/
│   │   └── types/
│   ├── styles/
│   └── main.tsx
├── public/
└── tests/
```

### 5.3 قواعد الحدود

- لا تستورد وحدة Frontend تفاصيل داخلية من وحدة أخرى.
- يسمح الاستيراد عبر Public API للوحدة فقط عند الحاجة.
- تبقى المكونات العامة في `shared/ui` محايدة عن منطق الأعمال.
- يبقى منطق الأعمال الخاص بوحدة داخل الوحدة نفسها.
- تحفظ الصفحات والتدفقات والنماذج والاستعلامات والاختبارات بجوار Feature التي تخدمها.
- يمنع إنشاء مجلدات عامة ضخمة باسم `components` أو `services` على مستوى التطبيق لكل الوظائف.
- يمنع استدعاء API مباشرة من المكونات البصرية العامة.
- تمنع Circular Dependencies ويجري فحصها آليًا.

### 5.4 إدارة أنواع الحالة

تستخدم الأداة المناسبة لكل نوع من الحالة:

| نوع الحالة | الأداة أو الموقع | القاعدة |
|---|---|---|
| Server State | TanStack Query v5 | المصدر هو API؛ تستخدم Queries وMutations وCache Invalidation |
| URL State | React Router search params and route state | الفلاتر والصفحات والفرز القابل للمشاركة يوضع في URL |
| Form State | React Hook Form | يبقى محليًا للنموذج ويستخدم Zod للتحقق عند الحاجة |
| Local UI State | `useState` أو `useReducer` | للحالة المؤقتة القريبة من المكون |
| Shared UI State | Zustand v5 عند الحاجة المثبتة | لا يستخدم لاستنساخ بيانات Server State |
| Cross-cutting Context | React Context | للهوية واللغة والاتجاه والتهيئة الثابتة نسبيًا |
| Derived State | يحسب أثناء Rendering أو Selector | لا يخزن كنسخة مكررة |

### 5.5 مبادئ React الملزمة

- تكون لكل قيمة State جهة ملكية واحدة واضحة.
- يمنع تكرار Server State في Zustand أو Context.
- يتجنب State المتناقض أو المتداخل بعمق أو القابل للاشتقاق.
- تستخدم Effects فقط للمزامنة مع نظام خارجي أو Browser API.
- لا يستخدم `useEffect` لاشتقاق بيانات يمكن حسابها أثناء Rendering.
- توضع State في أقرب مكون يحتاجها ولا ترفع إلى أعلى دون سبب.
- تستخدم المكونات Controlled عندما يتطلب التنسيق بين المكونات مصدر حقيقة واحدًا.
- تستخدم Error Boundaries على مستوى التطبيق والمسارات والوحدات الحرجة.
- تستخدم Suspense وLazy Loading وفق استراتيجية واضحة، وليس لتغطية تدفقات تحميل غير مفهومة.
- تستخدم Semantic HTML قبل ARIA متى كان ذلك ممكنًا.
- لا يعتمد اللون وحده لنقل الحالة.
- تختبر العربية والإنجليزية وRTL وLTR في التدفقات الأساسية.

### 5.6 React Compiler

React Compiler 1.x إصدار مستقر ويمكن استخدامه في الإنتاج. يعتمد المشروع التفعيل التدريجي وفق الآتي:

1. تفعيل `eslint-plugin-react-hooks` بالإعداد `recommended-latest`.
2. معالجة مخالفات Rules of React قبل تفعيل Compiler على نطاق واسع.
3. تجربة Compiler على وحدة أو مجموعة مسارات محدودة.
4. قياس الأداء وحجم البناء وسلوك الاختبارات.
5. التوسع بعد ثبوت الاستقرار.

بعد اعتماد Compiler:

- لا تستخدم `useMemo` و`useCallback` و`memo` بصورة تلقائية.
- تحفظ Manual Memoization فقط عندما توجد حاجة مثبتة أو تكامل يتطلب ثبات المرجع.
- يستخدم React Profiler وPerformance Tracks قبل إجراء تحسينات معقدة.
- لا تزال صحة الكود وحدود State أهم من تحسينات Compiler.

### 5.7 Routing وCode Splitting

- يستخدم React Router 8.2 من حزمة `react-router` وفق API الإصدار الحالي.
- يعرف Router مركزيًا بينما تملك كل وحدة Route Definitions الخاصة بها.
- تطبق Route-level Code Splitting على وحدات الأعمال والصفحات الثقيلة.
- تستخدم Lazy Imports للرسوم البيانية والمحررات والمكونات الكبيرة.
- تعرف Error Boundary وLoading behavior لكل Route حرجة.
- تطبق Authorization Guards على مستوى المسار والوظيفة، مع بقاء القرار الأمني النهائي في API.
- تحفظ الفلاتر والصفحات والفرز في Search Parameters عندما يجب مشاركة الرابط أو العودة إلى الحالة.

## 6. حزم Frontend المختارة

### 6.1 الحزم الأساسية

| الغرض | الحزمة أو التقنية | القرار |
|---|---|---|
| UI Runtime | `react` و`react-dom` 19.2.7 | Required |
| Routing | `react-router` 8.2 | Required |
| Build | Vite 8.1 | Required |
| Language | TypeScript 6.0 | Required |
| Styling | Tailwind CSS 4.3 | Required |
| Vite Tailwind integration | `@tailwindcss/vite` | Required |
| Server State | `@tanstack/react-query` v5 | Required |
| Forms | `react-hook-form` v7 | Required للـForms المركبة |
| Runtime schemas | Zod v4 | Required لعقود ونماذج محددة |
| Data tables | `@tanstack/react-table` v8 | Required للجداول المؤسسية المخصصة |
| Localization | `i18next` و`react-i18next` | Required |
| Entra authentication | `@azure/msal-browser` و`@azure/msal-react` | Required |
| Dates | `date-fns` | Recommended |
| Local shared UI state | `zustand` v5 | Conditional |
| Accessible primitives | Radix UI Primitives | Recommended عند الحاجة لمكونات Headless |
| Icons | Lucide React | Recommended |

تعتمد أحدث Patch مستقرة ومتوافقة من الحزم غير الأساسية عند إنشاء المشروع، ثم تثبت في ملف القفل. يجب ألا يؤدي وصف `v5` أو `v8` في هذه الوثيقة إلى تحديث تلقائي غير محكوم.

### 6.2 قرارات عدم الاستخدام الافتراضي

- لا يستخدم Redux افتراضيًا؛ يضاف فقط إذا ظهرت حاجة لا يغطيها توزيع الحالة المعتمد.
- لا يستخدم Axios افتراضيًا؛ يفضل Native Fetch مع Typed Client مولد من OpenAPI.
- لا يستخدم MUI أو إطار مكونات بصري شامل افتراضيًا؛ يعتمد Design System خاص بالصندوق باستخدام Tailwind.
- لا يستخدم CSS-in-JS افتراضيًا.
- لا تستخدم مكتبة Utility كاملة عندما تكفي وظائف JavaScript أو TypeScript القياسية.
- لا تستدعى Microsoft Graph أو Oracle Fusion مباشرة من المتصفح.

### 6.3 عميل API

يعتمد الآتي:

- يكون ASP.NET Core OpenAPI هو العقد المصدر.
- يولد Typed TypeScript Client في CI أو Build محكوم.
- لا تكتب الأنواع نفسها يدويًا في الواجهة والخادم.
- يستخدم Native Fetch أو Wrapper صغير موحد.
- تدار Queries وMutations عبر TanStack Query.
- توحد معالجة Problem Details وCorrelation IDs و401 و403 و429 و5xx.
- لا تعاد محاولة Mutations تلقائيًا إلا عندما تكون Idempotent ومصممة لذلك.

أداة توليد العميل النهائية مثل Orval أو `openapi-typescript` تحتاج قرارًا تنفيذيًا صغيرًا بعد اختبار توافقها مع OpenAPI الناتج من ASP.NET Core.

## 7. Tailwind CSS ونظام التصميم

### 7.1 طريقة الاستخدام

يستخدم Tailwind CSS 4.3 من خلال إضافة Vite الرسمية:

```ts
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
});
```

```css
@import "tailwindcss";
```

### 7.2 ضوابط التصميم

- تعرف Design Tokens للهوية والألوان والخطوط والمسافات والحواف والظلال والحركة.
- لا توزع قيم الألوان والعرض والارتفاع الاعتباطية دون مبرر.
- تستخدم Logical Properties ودعم RTL بدل إنشاء نسختين منفصلتين من كل Component.
- تبنى مكونات الصندوق في `shared/ui` مع Variants محدودة وواضحة.
- تستخدم أدوات مثل `clsx` و`tailwind-merge` فقط إذا احتاج نظام Variants إلى دمج Classes بصورة قابلة للضبط.
- يعتمد `class-variance-authority` فقط إذا ثبتت فائدته في تصميم Variants؛ ليس إلزاميًا.
- يمنع نسخ مكونات غير مراجعة أمنيًا أو بصريًا إلى النظام.
- يجب اجتياز جميع المكونات الأساسية فحص Keyboard وFocus وScreen Reader وContrast وRTL.

## 8. هوية المستخدم والأمن في الواجهة

- يستخدم Microsoft Entra ID من خلال MSAL.
- لا تحفظ Access Tokens في Local Storage.
- يفضل التخزين المؤقت في الذاكرة أو Session Storage وفق قرار الأمن ونموذج الجلسة.
- لا تعتبر إخفاء زر أو Route تفويضًا أمنيًا؛ يتحقق API من كل عملية.
- تستخدم App Roles أو Claims مع Policies في الخادم.
- تحفظ صلاحيات الأعمال الدقيقة في النظام عندما لا تكون مناسبة لإدارة Entra.
- تطبق Content Security Policy وسياسات Headers المناسبة.
- يمنع إدراج Secrets أو Client Secrets في تطبيق React.
- يستخدم Authorization Code Flow with PKCE للتطبيق العام.

## 9. حزم Backend الأساسية

| الغرض | التقنية أو الحزمة | القرار |
|---|---|---|
| Web API | ASP.NET Core 10 | Required |
| OpenAPI | `Microsoft.AspNetCore.OpenApi` | Required |
| Validation | `Microsoft.Extensions.Validation` | Required للقواعد البسيطة |
| Complex validation | FluentValidation 12.x | Conditional |
| Data access | `Microsoft.EntityFrameworkCore.SqlServer` 10.0.10 | Required |
| EF design tools | `Microsoft.EntityFrameworkCore.Design` 10.0.10 | Development only |
| Entra integration | Microsoft.Identity.Web 4.x | Required |
| Exchange integration | Microsoft Graph .NET SDK 6.x | Required |
| Resilient HTTP | `Microsoft.Extensions.Http.Resilience` | Required للتكاملات الخارجية |
| Caching | `Microsoft.Extensions.Caching.Hybrid` | Conditional |
| Observability | OpenTelemetry packages | Required |
| Structured logging | `Microsoft.Extensions.Logging` مع Provider معتمد | Required |
| Local orchestration | .NET Aspire AppHost and Service Defaults | Recommended للتطوير والاختبار |
| Background processing | Hosted Services كبداية | Required للـOutbox والمهام البسيطة |

لا تستخدم `FluentValidation.AspNetCore` القديمة. يدمج FluentValidation من خلال Validators وEndpoint Filters أو Pipeline خاص إذا كان مطلوبًا.

## 10. قاعدة البيانات SQL Server

- يعتمد SQL Server 2025 مع آخر Security Patch وCU معتمدين.
- تستخدم EF Core Migrations مع مراجعة SQL الناتج قبل الإنتاج.
- تمنع Migrations التلقائية عند تشغيل التطبيق في الإنتاج.
- تنفذ تغييرات Schema من خلال Pipeline نشر معتمد وقابل للرجوع.
- تستخدم Temporal Tables فقط للكيانات التي تستفيد منها بوضوح، ولا تستبدل سجل التدقيق الكامل.
- توضع Indexes بناء على الاستعلامات وخطط التنفيذ والقياس.
- تستخدم Pagination على الخادم، ولا تحمل الجداول المؤسسية بالكامل إلى المتصفح.
- تستخدم RowVersion أو آلية Concurrency مناسبة للسجلات الحساسة.
- تطبق تشفير الاتصال وإدارة حسابات الخدمة وأقل صلاحية.
- يحدد High Availability وBackup وRPO وRTO في التصميم التشغيلي.

## 11. التكاملات المعتمدة فقط

### 11.1 Oracle Fusion Cloud ERP

يغطي التكامل البيانات المالية والتجارية المعتمدة التي يملكها Oracle Fusion، مثل الميزانية والالتزامات والتكاليف والموردين وطلبات وأوامر الشراء والعقود والاستلامات والفواتير والمدفوعات، بعد اعتماد التصميم التفصيلي.

يجب أن يشمل التصميم:

- مصدر الحقيقة لكل عنصر بيانات؛
- اتجاه وتواتر التكامل؛
- المصادقة والتفويض؛
- Data Contracts وMappings؛
- Idempotency وإعادة المحاولة؛
- التسوية وحداثة البيانات؛
- معالجة الأخطاء والعزل وإعادة التشغيل؛
- التدقيق وCorrelation ID؛
- عدم تعديل البيانات المملوكة لـOracle محليًا دون عملية تصحيح معتمدة.

### 11.2 Microsoft Entra ID

يغطي:

- تسجيل الدخول الموحد؛
- المصادقة؛
- MFA والسياسات الشرطية وفق سياسة الصندوق؛
- App Registration وScopes وApp Roles؛
- إنهاء الجلسات وتعطيل الوصول؛
- ربط الهوية الخارجية بمعرف المستخدم الداخلي.

لا تعتمد مزامنة Groups أو الملف التنظيمي إلا إذا اعتمدت صراحة ضمن تصميم الهوية.

### 11.3 Microsoft Exchange

يستخدم Microsoft Graph من الخادم لأغراض:

- إرسال إشعارات البريد؛
- إنشاء وتحديث وإلغاء دعوات الاجتماعات؛
- إنشاء أحداث التقويم عند الحاجة؛
- التذكير والتصعيد؛
- حفظ معرف الرسالة أو الحدث للربط والتدقيق عند الحاجة.

لا تعد Exchange قاعدة بيانات للمشروع، ولا تحفظ فيها النسخة الرسمية من بيانات المشروع.

## 12. Observability والتشغيل

يطبق النظام:

- Structured Logs؛
- Metrics؛
- Distributed Traces؛
- Correlation IDs عبر الواجهة وAPI والتكاملات والـOutbox؛
- Health وReadiness Checks؛
- مراقبة Jobs والتكاملات وإعادة المحاولة؛
- تنبيهات تشغيلية قابلة للتوجيه والتصعيد؛
- إخفاء البيانات الحساسة من السجلات؛
- حفظ سجلات التشغيل وفق سياسة احتفاظ؛
- لوحات تشغيل للأخطاء والأداء والتوافر وحداثة التكاملات.

يستخدم .NET Aspire للتنسيق المحلي وService Defaults والمشاهدة أثناء التطوير والاختبار، دون افتراض أنه منصة الاستضافة الإنتاجية.

## 13. الاختبارات والجودة الهندسية

### 13.1 Frontend

| النوع | الأداة المقترحة |
|---|---|
| Unit and component tests | Vitest |
| Component behavior | React Testing Library |
| API mocking | Mock Service Worker |
| End-to-end | Playwright |
| Accessibility automation | axe-core مع اختبارات يدوية |
| Visual regression | TBD وفق أداة CI والمنصة |

### 13.2 Backend

| النوع | الأسلوب |
|---|---|
| Domain unit tests | اختبارات مباشرة لقواعد النطاق |
| Slice tests | اختبار Handler والتحقق والتفويض |
| Integration tests | SQL Server فعلي في Container أو بيئة معزولة |
| Functional API tests | تشغيل API واختبار HTTP كامل |
| Contract tests | Oracle Fusion وMicrosoft Graph |
| Architecture tests | منع كسر حدود الوحدات والتبعيات |
| Security tests | Authentication وAuthorization وInput وFiles وHeaders |
| Performance tests | سيناريوهات بأهداف NFR معتمدة |

### 13.3 قواعد الاختبار

- تختبر السلوك لا تفاصيل التنفيذ الداخلية.
- تعطى الأولوية لاختبارات التكامل والـFunctional في العمليات الحرجة.
- لا يعتمد InMemory Provider بديلًا عن SQL Server في اختبارات الاستعلامات المهمة.
- تستخدم بيانات اصطناعية أو مقنعة في البيئات غير الإنتاجية.
- تربط الاختبارات لاحقًا بمعرفات FR وNFR وVAL وSE وBI في مصفوفة التتبع.

## 14. DevOps وبنية المستودع

يقترح Monorepo واحد يحتوي Frontend وBackend والتوثيق:

```text
/
├── src/
├── web/
├── tests/
├── docs/
├── scripts/
├── Directory.Build.props
├── Directory.Packages.props
├── global.json
├── package.json
├── pnpm-workspace.yaml
├── pnpm-lock.yaml
└── README.md
```

الضوابط:

- جميع التغييرات من خلال Branch وPull Request.
- يشترط نجاح Build وLint وType Check والاختبارات قبل الدمج.
- تستخدم Conventional أو Intentional Commit Messages بصورة متسقة.
- ينفذ Dependency Review وLicense Scan وSecret Scan وSAST.
- تستخدم Environments وموافقات للنشر إلى UAT والإنتاج.
- تحفظ Artifacts وSBOM وأدلة النشر والاختبار.
- يطبق Zero-downtime أو Maintenance strategy وفق التصميم التشغيلي.
- توجد خطة Rollback للتطبيق وقاعدة البيانات والتهيئة.

## 15. قواعد TypeScript وReact

يعتمد `tsconfig` صارمًا، بما يشمل:

- `strict: true`؛
- عدم استخدام `any` إلا باستثناء موثق؛
- تفضيل `unknown` للمدخلات غير الموثوقة؛
- `noUncheckedIndexedAccess`؛
- `exactOptionalPropertyTypes` بعد اختبار توافق الحزم؛
- `noFallthroughCasesInSwitch`؛
- `noImplicitOverride` عند انطباقها؛
- `useDefineForClassFields`؛
- ESM وبناء متوافق مع Vite؛
- معالجة Deprecations في TypeScript 6.0 قبل الانتقال المستقبلي إلى TypeScript 7.

قواعد React:

- يمنع تحديث State أثناء Rendering.
- يمنع استدعاء Hooks شرطيًا.
- يمنع Mutating للـProps أوState.
- تستخدم Keys مستقرة من البيانات، وليس Index عند تغير الترتيب.
- لا تحول كل مكون إلى Custom Hook أو Context دون قيمة واضحة.
- تفصل المكونات البصرية عن Orchestration عندما يزيد التعقيد.
- تستخدم Composition بدل Props متضخمة أو Inheritance.
- توضع قواعد الأعمال في API والنطاق، ولا يعتمد المتصفح مرجعًا وحيدًا للحكم.

## 16. الأداء وتجربة المستخدم

- تعتمد Route وFeature Code Splitting.
- تقاس Core Web Vitals ومؤشرات تحميل الصفحات المؤسسية.
- تستخدم Virtualization للجداول والقوائم الكبيرة عند الحاجة.
- تستخدم Server-side Filtering وSorting وPagination للبيانات الكبيرة.
- تمنع Waterfalls غير الضرورية في طلبات API.
- تستخدم Prefetching بصورة موجهة بناء على التنقل المتوقع.
- تضبط Query `staleTime` وCache بحسب طبيعة البيانات، لا بقيمة عامة واحدة.
- تمنع إعادة المحاولات غير المحدودة.
- تستخدم Skeletons أوProgress indicators المناسبة مع رسائل واضحة.
- تحافظ على Focus بعد الانتقال والأخطاء والإجراءات.
- تعرض حداثة بيانات Oracle Fusion عند انطباقها.

## 17. الأمن وسلسلة التوريد

- تستخدم حزم من مصادر رسمية أو ناشرين موثوقين.
- تمنع الحزم غير المصانة أو مجهولة الترخيص أو ذات الاعتماديات المريبة.
- تفعل Dependabot أو Renovate وفق سياسة مراجعة.
- تنشأ SBOM لكل إصدار.
- توقع Artifacts أو تتحقق من سلامتها وفق منصة CI.
- تحفظ Secrets في Secret Store معتمد، وليس في Repository أو ملفات Frontend.
- تطبق Dependency Pinning وLockfile Integrity.
- تعالج ثغرات Critical وHigh وفق SLA الأمني المعتمد.

## 18. البدائل التي لم تعتمد

| البديل | القرار | السبب |
|---|---|---|
| Microservices من البداية | Rejected for baseline | تعقيد تشغيلي وتوزيع لا تبرره متطلبات حالية |
| Traditional layered architecture فقط | Rejected | تؤدي إلى فصل تقني أفقي وصعوبة تتبع حالات الاستخدام |
| Generic Repository | Rejected | يكرر تجريد EF Core ويحد قدراته |
| Mandatory MediatR | Deferred | Vertical Slices لا تتطلبه والقيمة والترخيص يحتاجان مراجعة |
| Redux كحالة عامة | Rejected as default | توزيع الحالة المعتمد يغطي Server وForm وURL وLocal State |
| Axios | Rejected as default | Native Fetch وTyped Client يقللان الاعتماديات |
| MUI كإطار تصميم رئيسي | Rejected as default | Tailwind وDesign System خاص يمنحان تحكمًا أفضل بهوية الصندوق |
| Next.js | Rejected for baseline | لا توجد حاجة مثبتة لـSSR أوRSC مع Backend مستقل في .NET |
| React Server Components | Out of baseline | تتطلب Runtime وخادم React وتزيد التعقيد دون حاجة مثبتة |
| Node.js 26 Current | Rejected for production | يستخدم Node.js 24 LTS للإنتاج وCI |
| .NET 11 Preview | Rejected for production | يستخدم .NET 10 LTS المدعوم |
| TypeScript 7 Preview | Rejected for production | يستخدم TypeScript 6.0 المستقر |

## 19. القيود والقرارات المفتوحة

| المعرف | السؤال أو القرار | المالك | الأثر | الحالة |
|---|---|---|---|---|
| TOQ-001 | ما نموذج الاستضافة والموقع والمنصة المعتمدة؟ | Enterprise Architecture / Operations | النشر والشبكات والأمن والتكلفة والتوافر | Open |
| TOQ-002 | ما أداة CI/CD والمستودع وArtifact Registry المعتمدة؟ | DevOps / IT | Pipeline والحزم والأدلة | Open |
| TOQ-003 | ما أهداف الأداء والسعة والتزامن والأحجام؟ | Business / Architecture | تصميم Frontend وAPI وSQL | Open |
| TOQ-004 | ما أهداف التوافر وRPO وRTO وساعات الخدمة؟ | Business / Operations | HA والنسخ والاستعادة | Open |
| TOQ-005 | ما معيار الوصول الحكومي والمستوى المطلوب؟ | Accessibility / UX | تصميم واختبار UI | Open |
| TOQ-006 | هل تستخدم Entra Groups في إسناد بعض الأدوار أم App Roles فقط؟ | IAM / Security | تصميم الصلاحيات والمزامنة | Open |
| TOQ-007 | ما طريقة وعقود Oracle Fusion المعتمدة لكل نطاق؟ | Oracle / Integration Owners | APIs والتواتر والتسوية | Open |
| TOQ-008 | هل يستخدم حساب Exchange تطبيقي مركزي أم إرسال بالنيابة عن المستخدم؟ | Messaging / Security | صلاحيات Graph والتدقيق | Open |
| TOQ-009 | ما أداة توليد TypeScript Client من OpenAPI؟ | Frontend / API Owners | العقود وDeveloper Experience | Open |
| TOQ-010 | ما أداة Structured Log وTelemetry Backend المعتمدة؟ | Operations / Security | المراقبة والاحتفاظ | Open |
| TOQ-011 | هل نحتاج مكون Rich Text Editor أوGantt أوCharts تجاريًا؟ | Product / UX / Procurement | الحزم والترخيص والأداء | Open |
| TOQ-012 | ما استراتيجية تخزين المرفقات داخل حدود عدم وجود تكامل ECM؟ | Architecture / Records | السعة والأمن والاحتفاظ | Open |

## 20. المراجع الرسمية للتحقق من الإصدارات

- React versions: `https://react.dev/versions`
- React Compiler: `https://react.dev/learn/react-compiler/introduction`
- React Router changelog: `https://reactrouter.com/start/start/changelog`
- Vite releases: `https://vite.dev/releases`
- Tailwind CSS blog: `https://tailwindcss.com/blog`
- TypeScript 6.0 release notes: `https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html`
- Node.js releases: `https://nodejs.org/en/about/previous-releases`
- .NET downloads: `https://dotnet.microsoft.com/en-us/download/dotnet/10.0`
- ASP.NET Core 10 release notes: `https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-10.0`
- EF Core 10 release notes: `https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-10.0/whatsnew`
- SQL Server latest updates: `https://learn.microsoft.com/en-us/troubleshoot/sql/releases/download-and-install-latest-updates`

## 21. سجل المراجعات

| الإصدار | التاريخ | المؤلف | ملخص التغيير |
|---|---|---|---|
| 0.1 | سابق | قالب المشروع | إنشاء قالب أولي للمكدس التقني. |
| 0.2 | 2026-07-18 | تحليل نظم ومعمارية حلول بمساعدة الذكاء الاصطناعي | اعتماد React و.NET وSQL Server وTailwind، وتوثيق Modular Monolith وVertical Slices ومعمارية Frontend والحزم والضوابط. |
