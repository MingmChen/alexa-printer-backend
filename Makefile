dev-install:
	cp .env.example .env
	pipenv install --dev

dev-serve:
	pipenv run dev-serve

serve:
	pipenv run serve