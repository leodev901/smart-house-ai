# frontend-next

`frontend`를 유지한 채, `frontend-next`를 Next.js App Router 정석 구조로 분리한 폴더입니다.

## 목표
- 기존 UI 디자인/문구/화면 흐름 유지
- `src/app` 기반 라우팅 구조 사용
- TypeScript + TSX 기준 유지보수 구조

## 구조
```ascii
frontend-next/
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── chatbot/page.tsx
│   │   ├── diagnosis/page.tsx
│   │   ├── contract/page.tsx
│   │   ├── news/page.tsx
│   │   ├── history/page.tsx
│   │   └── Dashboard/page.tsx    # 구 경로 호환용 리다이렉트
│   ├── components/
│   │   └── Sidebar.tsx
│   ├── global.d.ts
│   └── index.css
├── public/
│   └── config.js
├── next.config.mjs
├── tailwind.config.mjs
└── tsconfig.json
```

## 실행
```bash
cd frontend-next
npm install
npm run dev
```

## 빌드
```bash
npm run build
npm run start
```

## 참고
- `npm run dev`, `npm run build` 실행 전에 `.next`를 자동 정리하도록 설정되어 있습니다.
