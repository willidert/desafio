from rest_framework.routers import SimpleRouter
from desafio_sedecti import views


router = SimpleRouter()

router.register(r'pessoa', views.PessoaViewSet, 'Pessoa')

urlpatterns = router.urls
