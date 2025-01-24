# Form Configuration Page Wireframe Description

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
   - Page title: "Form Configuration"
     - Font size: 24px
     - Margin-bottom: 32px

2. **Side Navigation**
   - Navigation items:
     - Dashboard
     - Create New Campaign
     - Form Configuration (active)
     - Analytics
     - Settings

3. **Main Content Area**
   - **Objective Section**
     - Objective selection
     - AI-generated questions
     - Manual question addition
     - Question type selection

   - **Question Editor**
     - Question text input
     - Response type selection
     - Validation rules
     - Conditional logic
     - Preview button

   - **Form Flow Visualization**
     - Interactive flow diagram
     - Drag-and-drop question ordering
     - Branching logic visualization

   - **Preview Section**
     - Live form preview
     - Test functionality
     - Save button
     - Publish button

4. **Footer Section**
   - Back to Campaign Creation link
   - Help/Support link
   - Version number

## States
1. **Default State**
   - Empty question editor
   - Disabled publish button
   - Enabled save button

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
