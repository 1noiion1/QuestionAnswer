from rest_framework.permissions import BasePermission, SAFE_METHODS

class QuestionPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated or not user.role:
            return False

        role_perms = user.role.permission.value_list('codename', flat=True)


        if request.method is SAFE_METHODS:
            return 'view_question' in role_perms
        elif request.method == 'POST':
            return 'polls.add_question' in role_perms
        elif request.method in ('PUT', 'PATCH'):
            return 'polls.change_question' in role_perms
        elif request.method == 'DELETE':
            return 'polls.delete_question' in role_perms

        return False


class CanAnswerQuestion(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated or not user.role:
            return False

        return user.role.permissions.filter(codename='can_answer_question').exists()

