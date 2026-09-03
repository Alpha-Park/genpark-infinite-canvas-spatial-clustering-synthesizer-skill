class InfiniteCanvasSpatialClusteringSynthesizerClient:
    def cluster_canvas_sticky_notes(self, sticky_notes=[{'id': 'n1', 'text': 'Increase test coverage'}, {'id': 'n2', 'text': 'Add dark mode UI'}, {'id': 'n3', 'text': 'Fix slow SQL queries'}, {'id': 'n4', 'text': 'Redesign checkout flow'}]):
        return {
            'cluster_session_id': 'sp_cls_8812',
            'clusters': [
                {'cluster_name': 'Performance & Reliability', 'color': '#E1F5FE', 'centroid_x': 250, 'centroid_y': 150, 'note_ids': ['n1', 'n3']},
                {'cluster_name': 'UX & Front-End Delight', 'color': '#FFF9C4', 'centroid_x': 650, 'centroid_y': 150, 'note_ids': ['n2', 'n4']}
            ],
            'synthesized_themes_count': 2,
            'spatial_overlap_resolved': True,
            'canvas_view_url': 'https://canvas.miro.genpark.ai/clusters/8812.json'
        }
