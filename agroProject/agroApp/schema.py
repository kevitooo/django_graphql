import graphene
from graphene_django.types import DjangoObjectType
from .models import Work
from django.contrib.auth.decorators import login_required


# Crear un tipo de objeto de GraphQL para el modelo Work
class WorkType(DjangoObjectType):
    class Meta:
        model = Work


# Mutación para crear un trabajo
class CreateWork(graphene.Mutation):
    class Arguments:
        createAt = graphene.DateTime()
        recipe = graphene.String()

    work = graphene.Field(WorkType)

    def mutate(self, info, createAt, recipe):
        work = Work(createAt=createAt, recipe=recipe)
        work.save()

        return CreateWork(work=work)
    

# Mutación para actualizar un trabajo
class UpdateWork(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        createAt = graphene.DateTime()
        recipe = graphene.String()

    work = graphene.Field(WorkType)

    def mutate(self, info, id, createAt, recipe):
        work = Work.objects.get(pk=id)
        if createAt is "":
            raise Exception('Fecha de creación requerida')
        else:
            createAt = work.createAt
        if recipe is "":
            raise Exception('Receta requerida')
        else:
            work.recipe = recipe
        work.save()

        return UpdateWork(work=work)
    

# Mutación para eliminar un trabajo
class DeleteWork(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    work = graphene.Field(WorkType)

    def mutate(self, info, id):
        work = Work.objects.get(pk=id)
        work.delete()

        return DeleteWork(work=work)
    

# Mutación para crear, actualizar y eliminar un trabajo
class Mutation(graphene.ObjectType):
    create_work = CreateWork.Field()
    update_work = UpdateWork.Field()
    delete_work = DeleteWork.Field()


# Query para obtener todos los trabajos o por id
class Query(graphene.ObjectType):
    work = graphene.Field(WorkType, id=graphene.ID())
    all_works = graphene.List(WorkType)

    def resolve_work(self, info, id):
        return Work.objects.get(pk=id)

    def resolve_all_works(self, info):
        return Work.objects.all()
    