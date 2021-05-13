# rest-api

## `exploring django_restframework`

<p align='center'> Projects of this repo </p>

`1. serialization projects`

      - validation
         - validators
         - field level validation
         - object level validation

      - serializarTutorial (only api)
      - CRUDApp with validation (only api)

      - ModalSrApp model serializer with validation (only api)

`2. API View projects`

      - Function based apiview - FunctionApiViewCrud (only api)
      - Classed based apiview - same as functionbased apiview

      - Generic View using Mixin - GenericViewCrud ( only api )
      - Concrete View - ConcreteView ( only api )

      - Viewset class - ViewSetClass ( only api )
      - ModelViewSet Class - ModelViewSetClass ( only api )
      - ReadOnlyModelViewSet Class - Same as ModelViewSet class but only have list and retrive method

`3. Authentication and Permission projects`

      - Authentication
         - BasicAuthentication - BasicAuthenticationClass ( only api )
         - SessionAuthentication - SessionAuthenticationClass ( only api )
         - Authentication in Function based view - FunctionBasedViewAuthentication ( only api )
         - TokenAuthentication - TokenAuthenticationClass ( only api )
         - CustomAuthentication - Create a class which is subclass of BaseAuthentication and       override .authenticate(self, request) method.
         - JWT TOKEN - JWTTokenProject ( only api )

      - Permission
         - AllowAny
         - IsAuthenticated
         - IsAdminUser
         - IsAuthenticatedOrReadOnly
         - DjangoModelPermissions
         - DjangoModelPermissionsOrAnonReadOnly
         - DjangoObjectPermissions
         - CustomPermissions - customPermissionProject ( only api )
