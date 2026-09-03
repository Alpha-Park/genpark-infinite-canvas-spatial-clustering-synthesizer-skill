from client import InfiniteCanvasSpatialClusteringSynthesizerClient

def main():
    client = InfiniteCanvasSpatialClusteringSynthesizerClient()
    res = client.cluster_canvas_sticky_notes()
    print('Infinite Canvas Spatial Synthesizer: ' + res['cluster_session_id'])
    print('Themes Synthesized: ' + str(res['synthesized_themes_count']) + ' | Overlap Resolved: ' + str(res['spatial_overlap_resolved']))
    print('Canvas URL: ' + res['canvas_view_url'])

if __name__ == '__main__':
    main()
