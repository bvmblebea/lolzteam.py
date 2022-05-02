import requests
from typing import BinaryIO


class Lolzteam:
    def __init__(self, token: str):
        self.api = "https://api.lolz.guru"
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def get_categories_list(
            self,
            parent_category_id: int = None,
            parent_forum_id: int = None,
            order: str = "list"):
        url = f"{self.api}/categories&order={order}"
        if parent_category_id:
            url += f"&parent_category_id={parent_category_id}"
        if parent_forum_id:
            url += f"&parent_forum_id={parent_forum_id}"
        return requests.get(url, headers=self.headers).json()

    def get_category_info(self, category_id: int):
        return requests.get(
            f"{self.api}/categories/{category_id}",
            headers=self.headers).json()

    def get_forums_list(
            self,
            parent_category_id: int = None,
            parent_forum_id: int = None,
            order: str = "list"):
        url = f"{self.api}/forums&order={order}"
        if parent_category_id:
            url += f"&parent_category_id={parent_category_id}"
        if parent_forum_id:
            url += f"&parent_forum_id={parent_forum_id}"
        return requests.get(url, headers=self.headers).json()

    def get_forum_info(self, forum_id: int):
        return requests.get(
            f"{self.api}/forums/{forum_id}",
            headers=self.headers).json()

    def get_forum_followers(self, forum_id: int):
        return requests.get(
            f"{self.api}/forums/{forum_id}/followers",
            headers=self.headers).json()

    def follow_forum(
            self,
            forum_id: int,
            post: int = 0,
            alert: int = 1,
            email: int = 0):
        data = {
            "post": post,
            "alert": alert,
            "email": email
        }
        return requests.post(
            f"{self.api}/forums/{forum_id}/followers",
            data=data,
            headers=self.headers).json()

    def unfollow_forum(self, forum_id: int):
        return requests.delete(
            f"{self.api}/forums/{forum_id}/followers",
            headers=self.headers).json()

    def get_pages_list(self, parent_page_id: int, order: str = "list"):
        url = f"{self.api}/pages&order={order}"
        if parent_page_id:
            url += f"&parent_page_id={parent_page_id}"
        return requests.get(url, headers=self.headers).json()

    def get_page_info(self, page_id: int):
        return requests.get(
            f"{self.api}/pages/{page_id}",
            headers=self.headers).json()

    def get_navigation(self, parent_element_id: int = None):
        url = f"{self.api}/navigation"
        if parent_element_id:
            url += f"?parent={parent_element_id}"
        return requests.get(url, headers=self.headers).json()

    def get_threads_list(
            self,
            forum_id: int = None,
            thread_ids: str = None,
            creator_user_id: int = None,
            sticky: int = 0,
            thread_prefix_id: int = None,
            thread_tag_id: int = None,
            page: int = None,
            limit: int = None,
            order: str = None,
            thread_create_date: str = None,
            thread_update_date: str = None):
        url = f"{self.api}/threads?sticky={sticky}"
        if forum_id:
            url += f"&forum_id={forum_id}"
        if thread_ids:
            url += f"&thread_ids={thread_ids}"
        if creator_user_id:
            url += f"&creator_user_id={creator_user_id}"
        if thread_prefix_id:
            url += f"&thread_prefix_id={thread_prefix_id}"
        if thread_tag_id:
            url += f"&thread_tag_id={thread_tag_id}"
        if page:
            url += f"&page={page}"
        if limit:
            url += f"&limit={limit}"
        if order:
            url += f"&order={order}"
        if thread_create_date:
            url += f"&thread_create_date={thread_create_date}"
        if thread_update_date:
            url += f"&thread_update_date={thread_update_date}"
        return requests.get(url, headers=self.headers).json()

    def create_thread(
            self,
            forum_id: int,
            thread_title: str,
            content: str,
            thread_prefix_id: int = None,
            thread_tags: str = None):
        data = {
            "forum_id": forum_id,
            "thread_title": thread_title,
            "post_body": content
        }
        if thread_prefix_id:
            data["thread_prefix_id"] = thread_prefix_id
        if thread_tags:
            data["thread_tags"] = thread_tags
        return requests.post(
            f"{self.api}/threads",
            data=data,
            headers=self.headers).json()

    def upload_thread_attachment(
            self,
            forum_id: int,
            file: BinaryIO,
            attachment_hash: str = None):
        data = {
            "file": file.read(),
            "forum_id": forum_id
        }
        if attachment_hash:
            data["attachment_hash"] = attachment_hash
        return requests.post(
            f"{self.api}/threads/attachments",
            data=data,
            headers=self.headers).json()

    def delete_thread_attachment(
            self,
            forum_id: int,
            attachment_id: int,
            attachment_hash: str = None):
        url = f"{self.api}/threads/attachments?forum_id={forum_id}&attachment_id={attachment_id}"
        if attachment_hash:
            url += f"&attachment_hash={attachment_hash}"
        return requests.delete(url, headers=self.headers).json()

    def get_thread_info(self, thread_id: int):
        return requests.get(
            f"{self.api}/threads/{thread_id}",
            headers=self.headers).json()

    def delete_thread(self, thread_id: int):
        return requests.delete(
            f"{self.api}/threads/{thread_id}",
            headers=self.headers).json()

    def get_thread_followers(self, thread_id: int):
        return requests.get(
            f"{self.api}/threads/{thread_id}/followers",
            headers=self.headers).json()

    def follow_thread(self, thread_id: int, email: int = 0):
        data = {"email": email}
        return requests.post(
            f"{self.api}/threads/{thread_id}/followers",
            data=data,
            headers=self.headers).json()

    def unfollow_thread(self, thread_id: int):
        return requests.delete(
            f"{self.api}/threads/{thread_id}/followers",
            headers=self.headers).json()

    def get_thread_navigation(self, thread_id: int):
        return requests.get(
            f"{self.api}/threads/{thread_id}/navigation",
            headers=self.headers).json()

    def get_thread_poll_info(self, thread_id: int):
        return requests.get(
            f"{self.api}/threads/{thread_id}/poll",
            headers=self.headers).json()

    def vote_poll(
            self,
            thread_id: int,
            response_id: int,
            response_ids: str = None):
        data = {
            "response_id": response_id
        }
        if response_ids:
            data["response_ids"] = response_ids
        return requests.post(
            f"{self.api}/threads/{thread_id}/poll/votes",
            data=data,
            headers=self.headers).json()

    def get_poll_results(self, thread_id: int):
        return requests.get(
            f"{self.api}/threads/{thread_id}/poll/results",
            headers=self.headers).json()

    def get_new_threads(
            self,
            limit: int = 10,
            forum_id: int = None,
            data_limit: int = None):
        url = f"{self.api}/threads/recent?limit={limit}"
        if forum_id:
            url += f"&forum_id={forum_id}"
        if data_limit:
            url += f"&data_limit={data_limit}"
        return requests.get(url, headers=self.headers).json()

    def get_recent_threads(
            self,
            days: int = None,
            limit: int = 10,
            forum_id: int = None,
            data_limit: int = None):
        url = f"{self.api}/threads/recent?limit={limit}"
        if days:
            url += f"&days={days}"
        if forum_id:
            url += f"&forum_id={forum_id}"
        if data_limit:
            url += f"&data_limit={data_limit}"
        return requests.get(url, headers=self.headers).json()

    def get_thread_posts(
            self,
            thread_id: int = None,
            page_of_post_id: int = None,
            post_ids: str = None,
            page: int = None,
            limit: int = None,
            order: str = "natural"):
        url = f"{self.api}/posts?order={order}"
        if thread_id:
            url += f"&thread_id={thread_id}"
        if page_of_post_id:
            url += f"&page_of_post_id={page_of_post_id}"
        if post_ids:
            url += f"&post_ids={post_ids}"
        if page:
            url += f"&page={page}"
        if limit:
            url += f"&limit={limit}"
        return requests.get(url, headers=self.headers).json()

    def create_post(
            self,
            thread_id: int,
            quote_post_id: int = None,
            content: str = None):
        data = {
            "thread_id": thread_id,
            "post_body": content
        }
        if quote_post_id:
            data["quote_post_id"] = quote_post_id
        return requests.post(
            f"{self.api}/posts",
            data=data,
            headers=self.headers).json()

    def upload_post_attachment(
            self,
            file: BinaryIO,
            thread_id: int = None,
            post_id: int = None,
            attachment_hash: str = None):
        data = {"file": file.read()}
        if thread_id:
            data["thread_id"] = thread_id
        elif post_id:
            data["post_id"] = post_id
        elif attachment_hash:
            data["attachment_hash"] = attachment_hash
        return requests.post(
            f"{self.api}/posts/attachments",
            data=data,
            headers=self.headers).json()

    def get_post_info(self, post_id: int):
        return requests.get(
            f"{self.api}/posts/{post_id}",
            headers=self.headers).json()

    def edit_post(
            self,
            post_id: int,
            content: str,
            thread_title: str = None,
            thread_prefix_id: int = None,
            thread_tags: str = None,
            thread_node_id: int = None):
        data = {"post_body": content}
        if thread_title:
            data["thread_title"] = thread_title
        elif thread_prefix_id:
            data["thread_prefix_id"] = thread_prefix_id
        elif thread_tags:
            data["thread_tags"] = thread_tags
        elif thread_node_id:
            data["thread_node_id"] = thread_node_id
        return requests.put(
            f"{self.api}/posts/{post_id}",
            data=data,
            headers=self.headers).json()

    def delete_post(self, post_id: int):
        return requests.delete(
            f"{self.api}/posts/{post_id}",
            headers=self.headers).json()

    def get_post_attachments(self, post_id: int):
        return requests.get(
            f"{self.api}/posts/{post_id}/attachments",
            headers=self.headers).json()

    def delete_post_attachment(self, post_id: int, attachment_id: int):
        return requests.delete(
            f"{self.api}/posts/{post_id}/attachments/{attachment_id}",
            headers=self.headers).json()

    def get_post_likes(self, post_id: int, page: int = None, limit: int = 10):
        url = f"{self.api}/posts/{post_id}/likes?limit={limit}"
        if page:
            url += f"&page={page}"
        return requests.get(url, headers=self.headers).json()

    def like_post(self, post_id: int):
        return requests.post(
            f"{self.api}/posts/{post_id}/likes",
            headers=self.headers).json()

    def unlike_post(self, post_id: int):
        return requests.delete(
            f"{self.api}/posts/{post_id}/likes",
            headers=self.headers).json()

    def report_post(self, post_id: int, message: str):
        data = {"message": message}
        return requests.post(
            f"{self.api}/posts/{post_id}/report",
            data=data,
            headers=self.headers).json()

    def get_popular_tags(self):
        return requests.get(f"{self.api}/tags", headers=self.headers).json()

    def get_tags_list(self):
        return requests.get(
            f"{self.api}/tags/list",
            headers=self.headers).json()

    def get_tagged_content(
            self,
            tag_id: int,
            page: int = None,
            limit: int = 10):
        url = f"{self.api}/tags/{tag_id}?limit={limit}"
        if page:
            url += f"&page={page}"
        return requests.get(url, headers=self.headers).json()

    def get_filtered_tags_list(self, tag: str):
        return requests.get(
            f"{self.api}/tags/find?tag={tag}",
            headers=self.headers).json()

    def get_users_list(self, page: int = None, limit: int = 10):
        url = f"{self.api}/users?limit={limit}",
        if page:
            url += f"&page={page}"
        return requests.get(url, headers=self.headers).json()

    def register(
            self,
            email: str,
            username: str,
            password: str,
            user_dob_day: int = None,
            user_dob_month: int = None,
            user_dob_year: int = None,
            fields: str = None,
            client_id: str = None,
            extra_data: str = None,
            extra_timestamp: int = None):
        data = {
            "user-email": email,
            "username": username,
            "password": password
        }
        if user_dob_day:
            data["user_dob_day"] = user_dob_day
        elif user_dob_month:
            data["user_dob_month"] = user_dob_month
        elif user_dob_year:
            data["user_dob_year"] = user_dob_year
        elif fields:
            data["fields"] = fields
        elif client_id:
            data["client_id"] = client_id
        elif extra_data:
            data["extra_data"] = extra_data
        elif extra_timestamp:
            data["extra_timestamp"] = extra_timestamp
        return requests.post(
            f"{self.api}/users",
            data=data,
            headers=self.headers).json()

    def get_user_fields(self):
        return requests.get(
            f"{self.api}/users/fields",
            headers=self.headers).json()

    def find_user(self, username: str = None, user_email: str = None):
        url = f"{self.api}/users/find"
        if username:
            url += f"?username={username}"
        if user_email:
            url += f"?user_email={user_email}"
        return requests.get(url, headers=self.headers).json()

    def get_user_info(self, user_id: int):
        return requests.get(
            f"{self.api}/users/{user_id}",
            headers=self.headers).json()

    def edit_user(
            self,
            user_id: int,
            password: str = None,
            old_password: str = None,
            email: str = None,
            username: str = None,
            user_title: str = None,
            primary_group_id: int = None,
            secondary_group_ids: str = None,
            user_dob_day: int = None,
            user_dob_month: int = None,
            user_dob_year: int = None,
            fields: str = None):
        data = {}
        if password:
            data["password"] = password
        elif old_password:
            data["password_old"] = old_password
        elif email:
            data["user_email"] = email
        elif username:
            data["username"] = username
        elif user_title:
            data["user_title"] = user_title
        elif primary_group_id:
            data["primary_group_id"] = primary_group_id
        elif secondary_group_ids:
            data["secondary_group_ids"] = secondary_group_ids
        elif user_dob_day:
            data["user_dob_day"] = user_dob_day
        elif user_dob_month:
            data["user_dob_month"] = user_dob_month
        elif user_dob_year:
            data["user_dob_year"] = user_dob_year
        elif fields:
            data["fields"] = fields
        return requests.put(
            f"{self.api}/users/{user_id}",
            data=data,
            headers=self.headers).json()

    def upload_avatar(self, user_id: int, file: BinaryIO):
        data = {"avatar": file.read()}
        return requests.post(
            f"{self.api}/users/{user_id}/avatar",
            data=data,
            headers=self.headers).json()

    def delete_avatar(self, user_id: int):
        return requests.delete(
            f"{self.api}/users/{user_id}/avatar",
            headers=self.headers).json()

    def get_user_followers(self, user_id: int):
        return requests.get(
            f"{self.api}/users/{user_id}/followers",
            headers=self.headers).json()

    def follow_user(self, user_id: int):
        return requests.post(
            f"{self.api}/users/{user_id}/followers",
            headers=self.headers).json()

    def unfollow_user(self, user_id: int):
        return requests.delete(
            f"{self.api}/users/{user_id}/followers",
            headers=self.headers).json()

    def get_user_followings(
            self,
            user_id: int,
            order: str = "natural",
            page: int = None,
            limit: int = None):
        url = f"{self.api}/users/{user_id}/followings?order={order}"
        if page:
            url += f"&page={page}"
        if limit:
            url += f"&limit={limit}"
        return requests.get(url, headers=self.headers).json()

    def get_ignored_users(self):
        return requests.get(
            f"{self.api}/users/ignored",
            headers=self.headers).json()

    def ignore_user(self, user_id: int):
        return requests.post(
            f"{self.api}/users/{user_id}/ignore",
            headers=self.headers).json()

    def unignore_user(self, user_id: int):
        return requests.delete(
            f"{self.api}/users/{user_id}/ignore",
            headers=self.headers).json()

    def get_all_user_groups(self):
        return requests.get(
            f"{self.api}/users/groups",
            headers=self.headers).json()

    def get_user_groups(self, user_id: int):
        return requests.get(
            f"{self.api}/users/{user_id}/groups",
            headers=self.headers).json()

    def get_current_user(self):
        return requests.get(
            f"{self.api}/users/me",
            headers=self.headers).json()

    def get_user_contents(
            self,
            user_id: int,
            page: int = None,
            limit: int = 10):
        url = f"{self.api}/users/{user_id}/timeline?limit={limit}"
        if page:
            url += f"&page={page}"
        return requests.get(url, headers=self.headers).json()

    def create_profile_post(self, user_id: int, content: str):
        data = {"post_body": content}
        return requests.post(
            f"{self.api}/users/{user_id}/timeline",
            data=data,
            headers=self.headers).json()

    def get_profile_post_info(self, profile_post_id: int):
        return requests.get(
            f"{self.api}/profile-posts/{profile_post_id}",
            headers=self.headers).json()

    def edit_profile_post(self, profile_post_id: int, content: str):
        data = {"post_body": content}
        return requests.put(
            f"{self.api}/profile-posts/{profile_post_id}",
            data=data,
            headers=self.headers).json()

    def delete_profile_post(self, profile_post_id: int, reason: str = None):
        url = f"{self.api}/profile-posts/{profile_post_id}"
        if reason:
            url += f"?reason={reason}"
        return requests.delete(url, headers=self.headers).json()

    def get_profile_post_likes(self):
        return requests.get(
            f"{self.api}/profile-posts/{profile_post_id}/likes",
            headers=self.headers).json()

    def like_profile_post(self, profile_post_id: int):
        return requests.post(
            f"{self.api}/profile-posts/{profile_post_id}/likes",
            headers=self.headers).json()

    def unlike_profile_post(self, profile_post_id: int):
        return requests.delete(
            f"{self.api}/profile-posts/{profile_post_id}/likes",
            headers=self.headers).json()

    def get_profile_post_comments(self, before: str = None, limit: int = 10):
        url = f"{self.api}/profile-posts/{profile_post_id}/comments?limit={limit}"
        if before:
            url += f"&before={before}"
        return requests.get(url, headers=self.headers).json()

    def comment_profile_post(self, comment: str):
        data = {"comment_body": comment}
        return requests.post(
            f"{self.api}/profile-posts/{profile_post_id}/comments",
            headers=self.headers).json()

    def get_profile_post_comment(self, profile_post_id: int, comment_id: int):
        return requests.get(
            f"{self.api}/profile-posts/{profile_post_id}/comments/{comment_id}",
            headers=self.headers).json()

    def delete_profile_post_comment(
            self,
            profile_post_id: int,
            comment_id: int):
        return requests.delete(
            f"{self.api}/profile-posts/{profile_post_id}/comments/{comment_id}",
            headers=self.headers).json()

    def report_profile_post(self, profile_post_id: int, message: str):
        data = {"message": message}
        return requests.post(
            f"{self.api}/profile-posts/{profile_post_id}/report",
            data=data,
            headers=self.headers).json()

    def get_conversations(self, page: int = None, limit: int = 10):
        url = f"{self.api}/conversations?limit={limit}"
        if page:
            url += f"&page={page}"
        return requests.get(url, headers=self.headers).json()

    def create_conversation(
            self,
            conversation_title: str,
            recipients: str,
            content: str):
        data = {
            "conversation_title": conversation_title,
            "recipients": recipients,
            "message_body": content
        }
        return requests.post(
            f"{self.api}/conversations",
            data=data,
            headers=self.headers).json()

    def get_conversation_info(self, conversation_id: int):
        return requests.get(
            f"{self.api}/conversations/{conversation_id}",
            headers=self.headers).json()

    def delete_conversation(self, conversation_id: int):
        return requests.delete(
            f"{self.api}/conversations/{conversation_id}",
            headers=self.headers).json()

    def upload_conversation_attachment(
            self,
            file: BinaryIO,
            attachment_hash: str = None):
        data = {"file": file.read()}
        if attachment_hash:
            data["attachment_hash"] = attachment_hash
        return requests.post(
            f"{self.api}/conversations/attachments",
            data=data,
            headers=self.headers).json()

    def delete_conversation_attachment(
            self,
            attachment_id: int,
            attachment_hash: str = None):
        url = f"{self.api}/conversations/attachments?attachment_id={attachment_id}"
        if attachment_hash:
            url += f"&attachment_hash={attachment_hash}"
        return requests.delete(url, headers=self.headers).json()

    def get_conversation_messages(
            self,
            conversation_id: int,
            page: int = None,
            limit: int = None,
            order: str = None,
            before: str = None,
            after: str = None):
        url = f"{self.api}/conversation-messages?conversation_id={conversation_id}"
        if page:
            url += f"&page={page}"
        if limit:
            url += f"&limit={limit}"
        if order:
            url += f"&order={order}"
        if before:
            url += f"&before={before}"
        if after:
            url += f"&after={after}"
        return requests.get(url, headers=self.headers).json()

    def send_message(self, conversation_id: int, message: str):
        data = {
            "conversation_id": conversation_id,
            "message_body": message
        }
        return requests.post(
            f"{self.api}/conversation-message",
            data=data,
            headers=self.headers).json()

    def upload_message_attachment(
            self,
            file: BinaryIO,
            conversation_id: int = None,
            message_id: int = None,
            attachment_hash: str = None):
        data = {"file": file.read()}
        if conversation_id:
            data["conversation_id"] = conversation_id
        elif message_id:
            data["message_id"] = message_id
        elif attachment_hash:
            data["attachment_hash"] = attachment_hash
        return requests.post(
            f"{self.api}/conversation-messages/attachments",
            data=data,
            headers=self.headers).json()

    def get_message_info(self, message_id: int):
        return requests.get(
            f"{self.api}/conversation-messages/{message_id}",
            headers=self.headers).json()

    def edit_message(self, message_id: int, content: str):
        data = {"message_body": content}
        return requests.put(
            f"{self.api}/conversation-messages/{message_id}",
            data=data,
            headers=self.headers).json()

    def delete_message(self, message_id: int):
        return requests.delete(
            f"{self.api}/conversation-messages/{message_id}",
            headers=self.headers).json()

    def get_message_attachments(self, message_id: int):
        return requests.get(
            f"{self.api}/conversation-messages/{message_id}/attachments",
            headers=self.headers).json()

    def delete_message_attachment(
            self,
            message_id: int,
            attachment_id: int,
            conversation_id: int = None,
            attachment_hash: str = None):
        url = f"{self.api}/conversation-messages/{message_id}/attachments/{attachment_id}"
        if conversation_id:
            url += f"&conversation_id={conversation_id}"
        if attachment_hash:
            url += f"&attachment_hash={attachment_hash}"
        return requests.delete(url, headers=self.headers).json()

    def report_message(self, message_id: int, message: str):
        data = {"message": message}
        return requests.post(
            f"{self.api}/conversation-messages/{message_id}/report",
            data=data,
            headers=self.headers).json()

    def get_notifications(self):
        return requests.get(
            f"{self.api}/notifications",
            headers=self.headers).json()

    def get_notification_content(self, notification_id: int):
        return requests.get(
            f"{self.api}/notifications/{notification_id}/content",
            headers=self.headers).json()

    def send_custom_alert(
            self,
            user_id: int,
            message: str,
            notification_type: int = None,
            extra_data: str = None):
        data = {
            "user_id": user_id,
            "message": message
        }
        if notification_type:
            data["notification_type"] = notification_type
        elif extra_data:
            data["extra_data"] = extra_data
        return requests.post(
            f"{self.api}/notifications/custom",
            data=data,
            headers=self.headers).json()

    def mark_notification_read(self, notification_id: int = None):
        data = {}
        if notification_id:
            data["notification_id"] = notification_id
        return requests.post(
            f"{self.api}/notifications/read",
            data=data,
            headers=self.headers).json()

    def search_threads(
            self,
            query: str,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None,
            data_limit: int = None):
        data = {"q": query}
        if tag:
            data["tag"] = tag
        elif forum_id:
            data["forum_id"] = forum_id
        elif user_id:
            data["user_id"] = user_id
        elif page:
            data["page"] = page
        elif limit:
            data["limit"] = limit
        elif data_limit:
            data["data_limit"] = data_limit
        return requests.post(
            f"{self.api}/search/threads",
            data=data,
            headers=self.headers).json()

    def search_posts(
            self,
            query: str,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None,
            data_limit: int = None):
        data = {"q": query}
        if tag:
            data["tag"] = tag
        elif forum_id:
            data["forum_id"] = forum_id
        elif user_id:
            data["user_id"] = user_id
        elif page:
            data["page"] = page
        elif limit:
            data["limit"] = limit
        elif data_limit:
            data["data_limit"] = data_limit
        return requests.post(
            f"{self.api}/search/posts",
            data=data,
            headers=self.headers).json()

    def search_profile_posts(
            self,
            query: str,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None):
        data = {"q": query}
        if tag:
            data["tag"] = tag
        elif forum_id:
            data["forum_id"] = forum_id
        elif user_id:
            data["user_id"] = user_id
        elif page:
            data["page"] = page
        elif limit:
            data["limit"] = limit
        return requests.post(
            f"{self.api}/search/profile-posts",
            data=data,
            headers=self.headers).json()

    def search(
            self,
            query: str,
            tag: str = None,
            forum_id: int = None,
            user_id: int = None,
            page: int = None,
            limit: int = None):
        data = {"q": query}
        if tag:
            data["tag"] = tag
        elif forum_id:
            data["forum_id"] = forum_id
        elif user_id:
            data["user_id"] = user_id
        elif page:
            data["page"] = page
        elif limit:
            data["limit"] = limit
        return requests.post(
            f"{self.api}/search",
            data=data,
            headers=self.headers).json()

    def search_tagged(
            self,
            tag: str,
            tags: str = None,
            page: int = None,
            limit: int = None):
        data = {"tag": tag}
        if tags:
            data["tags"] = tags
        elif page:
            data["page"] = page
        elif limit:
            data["limit"] = limit
        return requests.post(
            f"{self.api}/search/tagged",
            data=data,
            headers=self.headers).json()
