# Campaign Creation Page Wireframe Description

## Layout
- Full-width layout with side navigation
- Main content area: 1200px max-width (responsive: 100% width on mobile)
- Side navigation width: 240px (collapsible on mobile)
- Padding: 32px (responsive: 16px on mobile)
- Spacing between sections: 24px

## Components
1. **Header Section**
   - ChatForm logo (left aligned)
   - User profile dropdown (right aligned)
   - Page title: "Create New Campaign"
     - Font size: 24px
     - Margin-bottom: 32px

2. **Side Navigation**
   - Navigation items:
     - Dashboard
     - Create New Campaign (active)
     - Analytics
     - Settings

3. **Main Content Area**
   - **Campaign Details Section**
     - Campaign Name input
     - Description textarea
     - Objective selection dropdown
     - Target audience definition
     - Advanced settings toggle

   - **Form Configuration Section**
     - Objective-driven question generation
     - Manual question addition
     - Question type selection
     - Response validation rules
     - Conditional logic setup

   - **Preview Section**
     - Live form preview
     - Test functionality
     - Save draft button
     - Publish button

4. **Footer Section**
   - Back to Dashboard link
   - Help/Support link
   - Version number

## States
1. **Default State**
   - Empty form fields
   - Disabled publish button
   - Enabled save draft button

2. **Loading State**
   - Spinner on save/publish buttons
   - Disabled form fields
   - Loading indicator

3. **Error State**
   - Error messages below invalid fields
   - Enabled retry button
   - Help/Support link highlighted

## Responsive Behavior
- Mobile: Single column layout
- Tablet: Two-column layout
- Desktop: Three-column layout
