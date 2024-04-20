# Event Manager Company: Software QA Analyst/Developer Onboarding Assignment

Issues Fixed
1. [Internal Server Error Occurs When Creating the user](https://github.com/SashankNallapareddy/event_manager/issues/1)
To address the internal server error encountered during user creation due to unexpected username format restrictions, I followed these steps:
    1. **Identified the Issue:**
      Upon investigating the error logs and reproducing the issue, it became evident that the application was failing to create users as expected.

    2. **Reviewed Database Migrations:**
      I examined the database migrations managed by Alembic to verify the database schema definition. It was observed that certain columns related to User Creation were missing or incorrect.

    3. **Updated Alembic Migrations:**
      I corrected the database schema by modifying the Alembic migrations. This involved adding the missing columns and updating the constraints to align with the desired User Table requirements.

    4. **Adjusted UserRole Enums:**
      Additionally, I ensured that the UserRole enums were updated accordingly to reflect any changes in the database schema. This step was crucial for maintaining consistency between the application code and the database structure.

    5. **Testing:**
      After making the necessary changes, I thoroughly tested the user registration endpoint. This involved sending requests to confirm that the application now correctly handled User creation without encountering internal server errors.

    6. **Verification:**
      Once testing was completed successfully, I verified that the application behaved as expected by creating users. By comparing the actual behavior against the expected behavior, I confirmed that the issue was resolved.

    7. **Pull Request Submission:**
      Finally, I compiled the changes into a pull request, providing a detailed description of the issue and the implemented solution. This allowed for peer review and ensured that the changes were properly documented and integrated into the codebase.

    By following these steps, I effectively addressed the internal server error during user creation by updating the database schema, correcting Alembic migrations, and verifying the changes through thorough testing.

  