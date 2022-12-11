from rest_framework.views import APIView, Request, Response, status
from .models import Team
from django.forms.models import model_to_dict


class TeamView(APIView):
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()

        return Response(teams.values())

    def post(self, request: Request) -> Response:
        team = Team.objects.create(**request.data)

        return Response(model_to_dict(team), status.HTTP_201_CREATED)


class TeamDetailView(APIView):
    # def __get_object(self, team_id: int) -> Team:
    #     try:
    #         team = Team.objects.get(id=team_id)
    #     except Team.DoesNotExist:
    #         return Response({"message": "Team not found"}, 404)

    #     return team

    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        # team = self.__get_object(team_id)

        return Response(model_to_dict(team), status.HTTP_200_OK)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        # team = self.__get_object(team_id)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()

        return Response(model_to_dict(team), status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        # team = self.__get_object(team_id)

        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
