# Wander Hub API
Wander Hub is a social media platform for travelers to share their trips, explore new places, and connect with other travel lovers. Users can easily create posts with stories and photos, like and comment on others posts, and save their favorites for later. The platform has a simple interface that allows for easy login, post management, and search options, ensuring it works well on all devices. 

The project is developed as a Portfolio Project 5 (Advanced Front End / React) for the Code Institute's Full Stack Software Development Course. The API supports the backend database, providing models and logic to enable the React frontend to perform CRUD operations.

![wander-hub-mockup-image]()
<br>
   - To see the API in a more user-friendly format, install a JSON extension such as [this one](https://chromewebstore.google.com/detail/jsonvue/chklaanhfefbnpoihckbnefhakgolnmc)

   - Link to the live API: [Wander Hub API](https://wanderhub-api-backend-8af792a9ebf9.herokuapp.com/)
   - Link to the live website: [Wander Hub Frontend](https://wanderhub-frontend-56da935583f2.herokuapp.com/)
   - Link to the Front-End Repository: [wanderhub-frontend](https://github.com/bhagyashriyogeshpatil/wanderhub-frontend)
---
# Table of Contents
- [Introduction](#introduction)
- [Agile Development Process](#agile-development-process)
    - [Agile Planning](#agile-planning)
      - [User Stories and Management](#user-stories-and-management)
      - [Milestones Overview](#milestones-overview)
- [The Structure Plane](#the-structure-plane)
  - [Features](#features)


---

## Introduction
Wander Hub is a social media platform where travelers can share their trips, discover new places, and connect with other travel lovers. The platform utilizes Django Rest Framework for the back-end and React for the front-end, ensuring a smooth user experience for creating, browsing, and interacting with travel content. This API provides a backend database (models and logic) to allow the frontend React application to perform CRUD operations. Users can easily create posts with stories and photos, interact by liking, commenting, and following others, and save their favorite posts for future reference.

Wander Hub has a user-friendly interface that makes it easy to use. It includes features like user login, the ability to create, update, and delete posts, and options to search and filter travel content. The platform is designed to work well on all devices, ensuring a smooth experience for everyone.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>* 

## Agile Development Process

### Agile Planning

For this project, I implemented an Agile methodology, organizing the entire process using a GitHub project board. This approach allowed me to manage the development from the initial planning stages to the final deployment. The project was divided into 6 milestones, each representing a key phase of the development process, ensuring that progress was systematic and aligned with the project’s goals.

You can view the entire Project Board, including all user stories and progress updates, here: <a href="https://github.com/users/bhagyashriyogeshpatil/projects/4" target="_blank">Github Project board</a>

<details><summary>User Story Template</summary>

![user story template](documentation/docs_images/user-story-template.png)
</details>

<details><summary>Kanban Board</summary>

![kanban board](documentation/docs_images/kanban-board.png)
</details>

#### **User Stories and Management:**

- **Acceptance Criteria:** 
Each user story was created with clear acceptance criteria to ensure that everyone understands what needs to be done. This approach guarantees that every task meets the required standards before it can be marked as complete.

- **MoSCoW Prioritization:** 
To effectively manage priorities, features were categorized using the MoSCoW method: 'Must have,' 'Should have,' and 'Could have.' This prioritization ensured that the essential features for the Minimum Viable Product (MVP) were developed first, while secondary features could be added if there was enough time.

- **User Stories Overview:** 
All user stories include:
  - **Acceptance Criteria:** Clearly defined requirements for completion.
  - **Labels for Prioritization:** Each feature is labeled as 'Must have,' 'Should have,' or 'Could have' to help prioritize development tasks.

- **Additional Labels:** 
I have also created two additional labels to show which tasks needed backend work and which needed frontend work:    
    - **API-backend** - for tasks related to backend API implementation
    - **React-frontend** - for tasks related to the frontend React app
Each user story was thoroughly checked to ensure it met the requirements before being closed.

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>* 

#### **Milestones Overview:** 
The development of Wander Hub is organized into six key milestones, each focusing on specific aspects of the project. Below is a detailed overview of each milestone along with the associated user story numbers:

**1. Project Setup and Deployment**
- This milestone focuses on setting up the project infrastructure and deploying the application.
  - User Story 1: Set up API Project
  - User Story 2: Set up Frontend Project
  - User Story 40: Deploy Project to Heroku
  - User Story 41: Create README.md File

**2. Basic UI/UX Elements**
- In this phase, I implemented essential user interface and experience elements to enhance usability.
  - User Story 3: Display Favicon in Browser Tab
  - User Story 4: Consistent Navigation Bar Across All Pages
  - User Story 5: Seamless Page Navigation

**3. User Authentication and Profile Management**
- This milestone is dedicated to user authentication and managing user profiles.
  - User Story 6: User Sign-Up
  - User Story 7: User Sign-In
  - User Story 8: Indicate Logged-In Status
  - User Story 9: Maintain Logged-In Status with Token Refresh
  - User Story 10: Conditional Rendering for Authentication Options
  - User Story 11: Display User Avatar
  - User Story 34: Edit Profile Details
  - User Story 35: Update Username and Password
  - User Story 37: Use Default Profile Image

**4. Post and Comment Features**
- This phase focuses on the core functionality for users to create and manage their posts and comments.
  - User Story 12: Create and Share Posts
  - User Story 13: View Post Details
  - User Story 14: Edit Own Posts
  - User Story 15: Delete My Posts
  - User Story 16: View Recent Posts
  - User Story 17: Search for Posts
  - User Story 20: Add Comments to Posts
  - User Story 21: Read Comments on Posts
  - User Story 22: Edit Own Comment
  - User Story 23: Delete Own Comment

**5. Interaction and Social Features**
- This milestone enhances social interactions within the platform, allowing users to connect and engage with each other.
  - User Story 18: Like Posts
  - User Story 19: Unlike Posts
  - User Story 24: Follow Users
  - User Story 25: Unfollow Users
  - User Story 26: Save Posts
  - User Story 27: Remove Saved Posts
  - User Story 28: Comment Reactions on Post
  - User Story 29: View Feed from Followed Users
  - User Story 30: View Liked Posts

**6. Extended User Features**
- The final milestone introduces advanced features to enhance the overall user experience.
  - User Story 31: View Other Users' Profiles
  - User Story 32: View User Statistics
  - User Story 33: View All Posts by a Specific User
  - User Story 36: View Most Followed Profiles
  - User Story 38: Infinite Scroll for Posts
  - User Story 39: Infinite Scroll for Comments

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>* 

## The Structure Plane

### Features
All features have been implemented with user stories in mind.  For a detailed overview of the fields included in each model for the API, visit the [Database Design](#database-design) section.

#### Homepage
- When users click the deployed link for the Wander Hub API, they are greeted with a welcome message.

![API_Homepage](documentation/docs_images/api_homepage.png)

*<span style="color: blue;">[Back to Content](#table-of-contents)</span>* 

#### Posts
- *As a logged-in user*, I want to create posts so that I can share my travel experience with the world! (User Story#12)
- *As a user*, I want to see a list of the most recent posts so that I can browse and stay updated with the latest content. (User Story#16)
- Posts are the main feature of the application, and all other functionalities are designed in relation to posts.
- You can access the posts list view here: https://wanderhub-api-backend-8af792a9ebf9.herokuapp.com/posts/

  - **Endpoint:** `/posts/`
  - **Methods Used:**
    - `GET` : Retrieves a list of posts.
    - `POST`: used to create posts
        
![API_Posts_View](documentation/docs_images/api_posts_list_view.png)
- With the help of serializers, the following additional fields have been added to the JSON data:
  - is_owner
  - profile_id
  - profile_image
- To see how people engage with each post, the following fields have been included:
  - like_id
  - savedpost_id
  - likes_count
  - comments_count
  - savedposts_count
- Filtering fields have been implemented to allow users to search and filter posts effectively.
- *As a user*, I want to search for posts using keywords so that I can find and learn more about posts and profiles that interest me. (User Story#17)
- The filtering options include:
  - Text search based on `owner_username`, `title`, `place`, and `region`.
  - Filter posts saved by the user to display their list of saved posts.
  - Filter posts liked by the user to see liked posts.
  - View posts from users the logged-in user is following.
  - View posts created by the user to see a list of their own posts.
  - Order the posts list by `likes_count`, `comments_count`, `savedposts_count`, `likes_created_at`, and `savedposts__created_at`
- *As a logged-in user*, I want to be able to edit my own posts so that I can make changes or updates after they are created. (User Story#14)
- *As a logged-in user*, I want to be able to delete my own posts so that I can remove any posts I no longer want to share.
- *As a user*, I want to click on a post to see its details so that I can learn more about it. (User Story#13)
  - **Endpoint:** `/posts/int:pk/`
  - **Methods Used:**
    - `GET`: Retrieves a specific post.
    - `PUT`: Edits/updates a post.
    - `DELETE`: Deletes a post.

![API_Posts_Detail_View](documentation/docs_images/api_posts_detail_view.png)

- Users can edit or delete their posts only when they are logged in. Logged-in users can also see the posts they've liked and saved. Everyone can view how many likes, comments, and saves each post has.

#### Profiles
- *As a user*, I want to view other users profiles so that I can see their posts and learn more about them. (User Story#31)
- *As a user*, I want to view detailed statistics about a specific user, including their bio and activity stats (such as number of posts, followers, and following), so that I can learn more about them. (User Story#32)
- You can access the profiles list view here: https://wanderhub-api-backend-8af792a9ebf9.herokuapp.com/profiles/
  - **Endpoint:** `/profiles/`
  - **Methods Used:**
    - `GET`: Retrieves a list of user profiles.

![Profiles_ListView](documentation/docs_images/api_profiles_list_view.png)

- The following fields are added through serializers to enhance the profile data in JSON format:
  - is_owner
  - following_id
  - posts_count
  - followers_count
  - following_count
- Profile creation is automatically handled by the system using Django's signal system. When a new `User` is created, a `Profile` is automatically generated for that user.
- When a user signs up, the `post_save` signal triggers a function that creates a profile for them. No manual action is needed from the user.
- Users can access the profile detail view by appending the profile ID to the `/profiles/` URL (e.g., `/profiles/1/`). If authorized (i.e., if the `is_owner` field is `true`), users can edit their own profiles.
- Each user’s profile displays their bio, profile avatar, the total number of posts (`posts_count`), the number of users they are following (`following_count`), and their total number of followers (`followers_count`).
- Backend filtering is implemented to allow users to:
  - Filter user profiles by those that are following the current user.
  - Filter user profiles by those that the current user is following, enabling the display of the most popular profiles on the front-end.
- *As a logged-in user*, I want to edit my profile details so that I can keep my information up to date. (User Story#34)
- *As a logged-in user* (profile owner), I want to update my username and password so that I can change my display name and maintain the security of my profile. (User Story#35)
- *As a user*, I want to have a default profile image so that I don’t need to upload my own immediately. (User Story#37)
  - **Endpoint:** `/profiles/<int:pk>/`
  - **Methods Used:**
    - `GET`: Retrieves the details of a specific user profile by ID.
    - `PUT`: Edits/updates the profile.

![Profiles_DetailView](documentation/docs_images/api_profiles_detail_view.png)

- If the user has not uploaded a profile picture, a default profile image is assigned to the image field. This ensures that every profile has a visual identifier, even without a custom avatar.