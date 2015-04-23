manage="${VENV}/bin/python ${INSTALLDIR}/${REPO}/django_mama_ng/manage.py"

$manage syncdb --noinput --migrate
$manage collectstatic --noinput
