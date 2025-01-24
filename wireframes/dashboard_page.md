# Dashboard Page Wireframe Description

## Layout
- Full-width layout with side navigation
- Main content area: 1200px max-width (responsive: 100% width on mobile)
- Side navigation width: 240px (collapsible on mobile)
- Padding: 32px (responsive: 16px on mobile)
- Grid layout for campaign cards: 3 columns (responsive: 1 column on mobile)
- Spacing between sections: 24px

## Authentication Integration
1. **Unauthenticated State**
   - Full-page overlay with Google OAuth button
   - Background blur effect
   - Google OAuth button (centered)
     - Size: 300px width, 48px height
     - Icon + "Continue with Google"
     - Border radius: 8px
   - Privacy policy and terms of service links below button

2. **Loading State**
   - Spinner animation on OAuth button
   - Disabled button state
   - Loading message: "Signing you in..."

3. **Error State**
   - Error message below OAuth button
   - Retry button enabled
   - Help/Support link

## Components
1. **Header Section**
   - ChatForm logo (left aligned)
     - Size: 120px width
     - Margin-right: 32px
   - User profile dropdown (right aligned)
     - Avatar: 40px diameter
     - Dropdown menu: 200px width
   - Page title: "Dashboard"
     - Font size: 24px
     - Margin-bottom: 32px

2. **Side Navigation**
   - Navigation items:
     - Dashboard (active)
     - Create New Campaign
     - Analytics
     - Settings
   - Each item:
     - Icon + Text
     - Padding: 12px 16px
     - Hover/active states

3. **Main Content Area**
   - **Campaign Statistics Overview**
     - 3-column grid (responsive: 1 column on mobile)
     - Cards:
       - Total Campaigns
       - Active Campaigns
       - Total Responses
     - Each card:
       - Icon + Metric + Label
       - Padding: 24px
       - Border radius: 8px

   - **Campaign List**
     - Search bar (top)
       - Width: 100%
       - Height: 48px
       - Placeholder: "Search campaigns..."
     - Campaign cards grid (3 columns)
       - Each card:
         - Campaign name
         - Response count
         - Status indicator
         - Last updated timestamp
         - Action buttons (Edit, View Analytics)
         - Padding: 16px
         - Border radius: 8px
         - Hover state

4. **Create New Campaign Button**
   - Fixed position (bottom right)
   - Size: 56px diameter
   - Icon: Plus symbol
   - Shadow effect
   - Hover animation

5. **Footer Section**
   - Copyright notice
   - Help/Support link
   - Version number
